from django.shortcuts import render
from .models import LearningMaterial

def add_learning(request):

    if request.method == "POST":

        title = request.POST['title']
        subject = request.POST['subject']
        topic = request.POST['topic']
        notes = request.POST['notes']
        link = request.POST['link']

        material = LearningMaterial.objects.create(
            user_id=1,
            title=title,
            subject=subject,
            topic=topic,
            notes=notes,
            link=link
        )

    return render(request, "add_learning.html")
