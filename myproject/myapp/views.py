from django.shortcuts import render

# Create your views here.
# start game fonk

def start_game(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        puzzle = generate_puzzle(image)
        request.session['name'] = name
        request.session['puzzle'] = puzzle
        request.session['moves'] = 0
        request.session['start_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return redirect('game')
    return render(request, 'game/start_game.html')


# play game fonk

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Puzzle

def play_game(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        puzzle_id = request.POST.get('puzzle_id')
        player_score = int(request.POST.get('player_score'))
        player, created = Player.objects.get_or_create(name=player_name)
        if not created:
            player.score += player_score
            player.save()
        puzzle = Puzzle.objects.get(id=puzzle_id)
        puzzle.correct += 1
        if puzzle.correct == puzzle.rows * puzzle.cols:
            puzzle.status = 'solved'
        puzzle.save()
        return JsonResponse({'success': True})
    else:
        puzzles = Puzzle.objects.all()
        context = {'puzzles': puzzles}
        return render(request, 'play_game.html', context)

# 

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image
import io

from .models import Player, Score

def home(request):
    if request.method == 'POST':
        # Get player name and uploaded image
        player_name = request.POST.get('player_name')
        uploaded_image = request.FILES.get('image')

        # Save the player
        player = Player(name=player_name)
        player.save()

        # Convert uploaded image to puzzle format
        image = Image.open(uploaded_image)
        cropped_images = []
        width, height = image.size
        cropped_width, cropped_height = width // 4, height // 4
        for i in range(4):
            for j in range(4):
                box = (j * cropped_width, i * cropped_height, (j + 1) * cropped_width, (i + 1) * cropped_height)
                cropped_images.append(image.crop(box))
        
        # Shuffle cropped images
        import random
        random.shuffle(cropped_images)

        # Save cropped images
        fs = FileSystemStorage()
        image_paths = []
        for i, cropped_image in enumerate(cropped_images):
            file_name = f"{player.id}_{i}.png"
            file_path = fs.save(file_name, io.BytesIO())
            image_paths.append(file_path)
        
        # Render game page
        context = {
            'player_id': player.id,
            'image_paths': image_paths,
        }
        return render(request, 'game.html', context)
    else:
        return render(request, 'home.html')

def save_score(request):
    if request.method == 'POST':
        # Get player and score
        player_id = request.POST.get('player_id')
        score = request.POST.get('score')

        # Save the score
        player = Player.objects.get(id=player_id)
        score = Score(player=player, score=score)
        score.save()

        return HttpResponse('Score saved!')
    else:
        return HttpResponse('Invalid request!')

#

from django.shortcuts import render, redirect
from .forms import StartGameForm
from .utils import convert_to_puzzle
import time

def start_game(request):
    """
    Starts the puzzle game.
    """
    if request.method == 'POST':
        form = StartGameForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            image = form.cleaned_data.get('image')
            puzzle = convert_to_puzzle(image)
            if puzzle:
                request.session['name'] = name
                request.session['puzzle'] = puzzle
                request.session['moves'] = 0
                request.session['start_time'] = time.time()
                request.session['game_over'] = False
                request.session.modified = True
                return redirect('game')
    else:
        form = StartGameForm()

    return render(request, 'start_game.html', {'form': form})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image

def play(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']

        # Yüklenen görseli yeniden boyutlandırma
        size = (480, 480)
        im = Image.open(image)
        im_resized = im.resize(size)

        # Yeniden boyutlandırılmış görseli geçici bir dosyada kaydetme
        im_resized_path = f'media/images/{name}.jpg'
        im_resized.save(im_resized_path, "JPEG")

        # Puzzle'ı oluşturma
        puzzle = create_puzzle(im_resized_path)

        # Skorları getirme
        scores = Score.objects.all().order_by('-score')[:10]

        context = {
            'name': name,
            'puzzle': puzzle,
            'scores': scores
        }

        return render(request, 'play.html', context)

    else:
        return redirect('home')

#from django.shortcuts import render
from .models import Puzzle

def puzzle(request):
    if request.method == 'POST':
        size = int(request.POST.get('size'))
        if size < 2:
            size = 2
        elif size > 10:
            size = 10
        puzzle = Puzzle(size)
        puzzle.create_solution()
        puzzle.shuffle()
        request.session['puzzle'] = puzzle
    elif request.method == 'GET':
        puzzle = request.session.get('puzzle')
        if not puzzle:
            puzzle = Puzzle(4)
            puzzle.create_solution()
            puzzle.shuffle()
            request.session['puzzle'] = puzzle

    board = puzzle.get_board()
    context = {
        'board': board,
        'size': puzzle.size,
        'moves': puzzle
    }

#

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
