from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .ThesisTopic import ThesisTopic

topics = [
    ThesisTopic(1, 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 
                'Yes', 'No', 'Yes', 'Yes', 'No', 
                'Artificial Intelligence, Machine Learning and Data Science', 
                'Machine learning approaches for Cyber Security', 
                'Bharanidharan Shanmugam'),
    ThesisTopic(9, 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 
                'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 
                'Artificial Intelligence, Machine Learning and Data Science', 
                'Informetrics applications in multidisciplinary domain', 
                'Yakub Sebastian'),
    ThesisTopic(16, 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 
                'No', 'No', 'No', 'Yes', 'No', 
                'Biomedical Engineering and Health Informatics', 
                'Development of a Virtual Reality System to Test Binaural Hearing', 
                'Sami Azam'),
    ThesisTopic(41, 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 
                'Yes', 'Yes', 'No', 'Yes', 'No', 
                'Cyber Security', 
                'Current trends on cryptomining and its potential impact on cryptocurrencies', 
                'Sami Azam'),
    ThesisTopic(176, 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 
                'No', 'No', 'No', 'Yes', 'No', 
                'Artificial Intelligence, Machine Learning and Data Science', 
                'Artificial Intelligence in Health Informatics', 
                'Asif Karim'),
    ThesisTopic(180, 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 
                'No', 'No', 'No', 'Yes', 'No', 
                'Artificial Intelligence, Machine Learning and Data Science', 
                'Unsupervised Model Development from Autism Screening Data', 
                'Asif Karim'),
    ThesisTopic(226, 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 
                'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 
                'Artificial Intelligence, Machine Learning and Data Science', 
                'Applying Artificial Intelligence to solve real world problems', 
                'Bharanidharan Shanmugam'),
]

def project_list(request):
    #  instances of ThesisTopic for each entry
    

    # Add topics to the context for rendering
    context = {'topics': topics}
    return render(request, 'Main/project_list.html', context)




def project_detail(request, topic_id):
    # Find the topic by its ID
    topic = next((t for t in topics if t.topic_number == topic_id), None)
    if topic is None:
        raise Http404("Topic does not exist")
    
    context = {'topic': topic}
    return render(request, 'Main/project_detail.html', context)