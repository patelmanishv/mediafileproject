from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('media_demo:upload_file')  # Redirect to the upload page
    else:
        form = FileUploadForm()
    return render(request, 'media_demo/upload.html', {'form': form})
