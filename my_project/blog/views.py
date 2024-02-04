from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only = False,logic_adapters=['chatterbot.logic.BestMatch'])
'''
list_to_train = [
    'hello take a breath and relax',
    'tell me about your daily habits',
    "I usually sleep late and wake up late in the afternoon ",
    "Try to do yoga and meditation it will improve your mental health,Tell me more about you",
    " I am student and I am suffering from guilt that I have wasted time",
    "Relax,You have lot of start with new energy and be consistent",
    "Not feeling well",
    "relax take a breath",
]'''



#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train('chatterbot.corpus.english.conversations','chatterbot.corpus.english.emotion','chatterbot.corpus.english.psychology')


def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse("This is a specific url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)