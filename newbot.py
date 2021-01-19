#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.


# -*- coding: utf-8 -*-
"""torch-chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6DJ6ecYNIrFX-dDFbD1dq8Jfba5-jdi
"""

intents = {
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for asking",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you later", "Goodbye"],
      "responses": [
        "See you later, thanks for asking",
        "Have a nice day",
        "Bye! Come back again soon."
      ]
    },
    {
      "tag": "thanks",
      "patterns": ["Thanks", "Thank you", "That's helpful", "Thank's a lot!"],
      "responses": ["Happy to help!", "Any time!", "My pleasure"]
    },
    {
      "tag": "funny",
      "patterns": [
        "Tell me a joke!",
        "Tell me something funny!",
        "Do you know a joke?"
      ],
      "responses": [
        "Why did the hipster burn his mouth? He drank the coffee before it was cool.",
        "What did the buffalo say when his son left for college? Bison."
      ]
    },
    {
      "tag": "girls",
      "patterns": [
        "Is there any special incentive given to girl students?",
        "whats special for girls?",
        "Is there any scholarship for girl students?"
      ],
      "responses": [
        "YES! If you are admitted to IIT Mandi, you will get a merit scholarship including full tuition fee waiver and Rs. 1,000/- per month stipend in the first year irrespective of category and parent’s income. This merit scholarship will continue for all 4 years of B.Tech. subject to good academic performance of the candidate indicated by a minimum SGPA criteria of 7.0 for the previous two semesters and no disciplinary action."
      ]
    },
    {
      "tag": "accomodation",
      "patterns": [
        "Where will the freshers be accommodated?",
        "In which campus will the freshers be going to?",
        "Accomodation?"
      ],
      "responses": [
        "The freshers will be accommodated at North Campus, Kamand.",
        "North Campus"
      ]
    },
    {
      "tag": "campus development",
      "patterns": [
        "How developed is the IIT Mandi campus at Kamand?",
        "Is the campus developed?"
      ],
      "responses": [
        "Phase 1 construction of the south campus is complete and the north campus is expected to complete in 2021."
      ]
    },
    {
      "tag": "weather",
      "patterns": [
        "How's the weather at IIT Mandi?",
        "How is the weather in Kamand like?",
        "Weather?"
      ],
      "responses": [
        "Weather becomes chilly after mid-October, and in winter, there is the occasional snowfall, especially in the mountains above Kamand. But in general, we have long winter vacations from early December till mid-February to keep the cold at bay. The weather is usually pleasant, especially in the evenings and is ideal for nature enthusiasts who want to explore the serene surroundings of IIT Mandi."
      ]
    },
    {
      "tag": "branch change",
      "patterns": [
        "How easy is the branch change in IIT Mandi?",
        "What is the branch change policy?",
        "How can I change my branch?",
        "Branch change policy"
      ],
      "responses": [
        "kindly have a look at the link below: http://iitmandi.ac.in/academics/branch_change.php"
      ]
    },
    {
      "tag": "MCM scholarship",
      "patterns": [
        "What is the procedure for getting the MCM scholarships?",
        "How to get scholarships?",
        "Are there any scholarships?"
      ],
      "responses": [
        "details can be found here: http://iitmandi.ac.in/academics/scholarship.php"
      ]
    },
    {
      "tag": "courses",
      "patterns": [
        "What will be the courses in 1st sem of B.Tech?",
        "Which courses will we study?",
        "What are the courses?"
      ],
      "responses": [
        "More about curriculum and courses: http://www.iitmandi.ac.in/academics/courses.php, http://iitmandi.ac.in/academics/perspective_btech_curriculum.php"
      ]
    },
    {
      "tag": "Laptops",
      "patterns": [
        "Can freshers bring laptops in the first sem?",
        "Are laptops allowed?",
        "Which laptops should we buy?"
      ],
      "responses": [
        "Yes. There is no restriction in bringing a laptop to the Institute when you join. It would be better if you had a laptop"
      ]
    },
    {
      "tag": "Internet",
      "patterns": [
        "Is there availability of internet on campus?",
        "How is the internet there?",
        "Do we have good internet speed?"
      ],
      "responses": [
        "Yes. The Internet is pretty good in the Institute and is uncapped, i.e., unlimited hi-speed net at all times."
      ]
    },
    {
      "tag": "hostel facilities",
      "patterns": [
        "What do we get in hostels?",
        "10. What facilities are provided to the freshers for the purchase of hostel necessities like mattresses, pillows, buckets etc.?",
        "What do we need to bring to the hostels?"
      ],
      "responses": [
        "Institute arranges for the sale of hostel necessities like mattresses, pillows, pillow covers, bed sheets, locks, buckets, mugs etc. on Orientation day. Local vendors are arranged for the sale of these items inside the Institute."
      ]
    },
    {
      "tag": "people in hostel",
      "patterns": [
        "How many people will stay in a hostel room?"
      ],
      "responses": [
        "Hostels have rooms of different sizes, single, double and triple occupancy. First year students usually get a shared room."
      ]
    },
    {
      "tag": "books",
      "patterns": [
        "Will we be buying books or we can get them from the library?",
        "Do we need to buy books?",
        "Are we required to bring any books?"
      ],
      "responses": [
        "In general, you can get the e-books for the materials that the teacher specifies. Also, you can get them from the library."
      ]
    },
    {
      "tag": "holidays",
      "patterns": [
        "What is the holiday schedule of IIT Mandi?",
        "When do we have holidays?",
        "When do we have vacations?"
      ],
      "responses": [
        "We have a five-day working week, and at times there are other holidays in between too. Semester breaks are from December to Mid February for winters and from mid June to early August in summers. Checkout our calender for more details: http://iitmandi.ac.in/academics/calendar.php"
      ]
    },
    {
      "tag": "activities",
      "patterns": [
        "What are the co-curricular activities and clubs at IIT Mandi?",
        "Are there any activities in IIT Mandi?",
        "What activities can we do there?",
        "What are the clubs at IIT Mandi?",
        "What are the different societies in IIT Mandi?"
      ],
      "responses": [
        "The student Gymkhana organizes all extracurricular activities. We have several different clubs like programming, robotronics, art, dance, music, dramatics, photography, design, mechanical and several others! Have a look at the link below for more details: https://gymkhana.iitmandi.co.in/"
      ]
    },
    {
      "tag": "sports",
      "patterns": [
        "What about sports?",
        "What sports can we play there?",
        "Sports equipment?",
        "What different games are available in IIT Mandi?"
      ],
      "responses": [
        "We play almost every sport you can imagine! We also have dedicated coaches for training!"
      ]
    },
    {
      "tag": "reach IIT Mandi",
      "patterns": [
        "How to reach from Delhi/Chandigarh to Mandi?",
        "How to reach IIT Mandi?",
        "Where is IIT Mandi?"
      ],
      "responses": [
        "Mandi is easily accessible from the two places by bus or by cab. From Delhi ISBT(Kashmiri gate) there is a regular bus service: Volvo, Tata AC and ordinary buses go directly to Mandi. Same is the case for Chandigarh; besides, all buses from Delhi pass through Chandigarh. You can also take the train to Chandigarh, and from there from the ISBT at Sector 43 to Mandi by bus. At Mandi ISBT, you are right in front of our Transit Campus. From there take the Institute shuttle service to Kamand campus."
      ]
    },
    {
      "tag": "session start",
      "patterns": [
        "When is the session starting for first year B.Tech students?",
        "When will our academic session start?",
        "When do our classes begin?"
      ],
      "responses": [
        "First semester will start in the online mode in November. Joining date would be updated soon."
      ]
    },
    {
      "tag": "Hangout",
      "patterns": [
        "What are the good places to hang out in Mandi town?",
        "Where can we chill in Mandi?"
      ],
      "responses": [
        "Mandi has a fairly good market, which can provide you with almost anything. Hotels like Raj Mahal, Regent Palms, Treat are good for dinners. Dominos, Raman Bakers, Sai Sweets have their share of fast food fanatics. Indira Market, built around a sunken lake, - the Mandi version of a super mall - is a delightful place for making little discoveries."
      ]
    },
    {
      "tag": "Ragging",
      "patterns": [
        "Is there Ragging?",
        "How is the ragging scenario at IIT Mandi?"
      ],
      "responses": [
        "Zero Tolerance for ragging. We have the following committees to take care of any issues, Student Welfare and Disciplinary Committee (SWDC), Anti-Ragging Committee (ARC)."
      ]
    },
    {
      "tag": "health",
      "patterns": [
        "Is there a dedicated health centre?",
        "What if someone gets hurt?",
        "What are the medical facilities at IIT Mandi?",
        "How is the medical staff at IIT Mandi?"
      ],
      "responses": [
        "There's absolutely no need to worry! We have a trained and dedicated medical staff to take care of basic health issues. Also we have specialist visits frequently."
      ]
    },
    {
      "tag": "food",
      "patterns": [
        "How is the mess food?",
        "Are there canteens?",
        "How many restaurants are there?",
        "What are the eating options there?",
        "Is there availability of veg food?",
        "Is the food nutritious?"
      ],
      "responses": [
        "The mess food is nutritional and offers a huge variety from mattar paneer to chole bhature to non veg food and not to mention the special dinner at every month's end. There are canteens for a change too!"
      ]
    },
    {
      "tag": "hostel timings",
      "patterns": [
        "Hostel timings?",
        "What time do hostels close?"
      ],
      "responses": [
        "24 hrs open, need to give attendance between 10pm to midnight, permission to be sought if going away. No alcohol or smoking."
      ]
    },
    {
      "tag": "wild animals",
      "patterns": [
        "Are there wild animals in IIT Mandi?",
        "Wild animals there?",
        "Snakes?"
      ],
      "responses": [
        "The campus is safe. No incident involving wild animals has been reported so far."
      ]
    },
    {
      "tag": "Unique activities",
      "patterns": [
        "What else can be done at IIT Mandi?",
        "Unique activities?"
      ],
      "responses": [
        "Due to its pristine location, students can enjoy hiking and trekking, mountain biking etc. We have active student clubs who coordinate these activities."
      ]
    },
    {
      "tag": "Placement",
      "patterns": [
        "What are the placement statistics of IIT Mandi?",
        "What is the highest package?",
        "Placement scenario?"

      ],
      "responses": [
        "80-90% students who opt for placement get placed. Salary package comparable to other IITs. Students go for higher studies, entrepreneurship etc Last year Placement in CSE was 98.27 %, EE was 84.5%, ME was 66.6% , CE 33.3%. Median Salary: 14LPA"
      ]
    },
    {
      "tag": "research",
      "patterns": [
        "Labs & research facilities at IIT Mandi",
        "What kind of reasearch does IIT Mandi do?"
      ],
      "responses": [
        "IIT Mandi has excellent teaching and research labs. Since the labs are newly developed, they have new and updated equipments."
      ]
    },
    {
      "tag": "teaching",
      "patterns": [
        "How good is the faculty in teaching?",
        "I heard that IIT Mandi has only fresh, young faculty. Will I get good teaching?",
        "How experienced are the teachers?"
      ],
      "responses": [
        "In any IIT, you will find a few teachers who inspire you because you have an interest in the subject. We have young faculty who are active in cutting-edge research and worked in excellent research labs and industry in India and abroad. Young faculty are easy to approach informally outside the classroom, they participate in sports etc. IIT Mandi has 10% senior faculty who mentor the young faculty so that their teaching is good and is improving. Many of the young faculty now have 4-7 years of teaching experience"
      ]
    },
    {
      "tag": "semester exchange",
      "patterns": [
        "Is it possible to do a semester in some other university?",
        "What are the opportunities for semester exchange with other national and international Institutes?"
      ],
      "responses": [
        "A:MoU with TU9 institutes Germany, WPI Universities in USA, Universities in Sweden, Denmark, Switzerland, Canada as well as other IITs. Students go for exchange programs for 1 or 2 semesters. More info: https://students.iitmandi.ac.in/international.php"
      ]
    },
    {
      "tag": "Data science",
      "patterns": [
        "What do they teach in data science?",
        "What are the new branches in IIT Mandi?"
      ],
      "responses": [
        "Hey! Check this out: http://iitmandi.ac.in/academics/courses.php"
      ]
    },
    {
      "tag": "induction",
      "patterns": [
        "Is there an induction program?",
        "What do we learn in the induction program?",
        "What is 5WIP?"
      ],
      "responses": [
        "We have a unique induction program where you get to learn several life skills. You will soon get to know about it more!"
      ]
    },
    {
      "tag": "PC club",
      "patterns": [
        "What is the programming club?",
        "What do you do at programming club",
        "What happens at PC?",
        "Does IIT Mandi have a programming club?",
        "How can I join the programming club?",
        "Do I need any pre-requisite to join the programming club?"
      ],
      "responses": [
        "We at programming club do all sorts of cool stuff from competitive programming, development, AI and ML, and cybersecurity. We hold several events and sessions related to all these and they are free for anyone and everyone to enjoy!! check us out at: https://pc.iitmandi.co.in/"
      ]
    },
    {
      "tag": "basic programming",
      "patterns": [
        "Which language should I start?",
        "Which programming language should I learn?",
        "How to start programming?",
        "Which is the easiest language to begin with?"
      ],
      "responses": [
        "Hey! Its good to know that you want to learn programming. You could start with C or python. There are several good playlists on youtube!",
        "C and Python are good languages for a beginner to learn. Checkout thenewboston's videos on C or Corey Schafer's videos on Python!"
      ]
    },
    {
      "tag": "vscode",
      "patterns": [
        "I have a problem in vscode.",
        "How to configure vscode to run c?",
        "How to configure vscode to run c++?",
      ],
      "responses": [
        "check this out: https://code.visualstudio.com/docs/languages/cpp"
      ]
    },
    {
      "tag": "presentation error",
      "patterns": [
        "My code is showing presentation error.",
        "What do we mean by a presentation error?",
        "Why am I getting a presentation error?",
        "vscode shows correctly, but when I submit, it shows presentation error."
      ],
      "responses": [
        "Presentation error happens when you forget to put newlines or do not follow the printing instructions of a question. Try reading the problem once again and checking your code!"
      ]
    },
    {
      "tag": "WA",
      "patterns": [
        "My code is showing wrong answer.",
        "What do we mean by a WA?",
        "Why am I getting a WA?",
        "vscode shows correctly, but when I submit, it gives WA.",
        "Why am I getting 100% wrong answer?",
        "Why am I getting 5% WA?"
      ],
      "responses": [
        "WA happens when your code doesn't run against all system test cases correctly. This means that the algorithm might not be correct, or you might be missing some corner cases. Try a few manual cases and see if you can find your own mistake, else you can talk to a senior. They are always glad to help!"
      ]
    },
    {
      "tag": "TLE",
      "patterns": [
        "My code is showing time limit exceeded.",
        "What do we mean by a TLE?",
        "Why am I getting a TLE?",
        "vscode shows correctly, but when I submit, it gives TLE."
      ],
      "responses": [
        "TLE happens when your code isn't optimised. This means that the algorithm might not be as efficient as it should be. Check this out: https://www.geeksforgeeks.org/overcome-time-limit-exceedtle/"
      ]
    },
    {
      "tag": "RTE",
      "patterns": [
        "My code is showing runtime error.",
        "What do we mean by a RTE?",
        "Why am I getting a SIGSEV?",
        "vscode shows correctly, but when I submit, it gives RTE.",
        "I am getting a segmentation fault."
      ],
      "responses": [
        "Check this out: https://www.geeksforgeeks.org/runtime-errors/"
      ]
    }
  ]
}

import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out

import numpy as np
import random
from torch.utils.data import Dataset, DataLoader

all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to xy pair
        xy.append((w, tag))

# stem and lower each word
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

#print(len(xy), "patterns")
#print(len(tags), "tags:", tags)
#print(len(all_words), "unique stemmed words:", all_words)

# create training data
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
#print(input_size, output_size)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        # if y would be one-hot, we must apply
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


#print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def chat(sentence):
    bot_name = "GCS-Bot"
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return (f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        return (f"{bot_name}: I do not understand...")


######################################################################
######################################################################
######################################################################

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(chat(update.message.text))


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1574443175:AAGjqZv6NX-fcZzm6Hod2VGPq44PgnGaP8A", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
