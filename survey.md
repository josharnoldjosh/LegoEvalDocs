# Survey Page

## The Basic Survey Page

Below is the basic survey page, and how to use it. Data will automatically be saved into the `state`.

#### build.py

```python
# build.py

from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment

# ...

survey = Survey(title="Example Survey")

text1 = Text("name", "What is your name?")
survey.questions.append(text1.toJson())

radioGroup1 = RadioGroup("major", "What is your major?", ["Computer Science", "Biology", "Philosophy", "Art History"])
survey.questions.append(radioGroup1.toJson())

checkBox1 = CheckBox("majors", "What are your majors?",
                     ["Computer Science", "Biology", "Philosophy", "Art History", "Music"], True)
survey.questions.append(checkBox1.toJson())

rating1 = Rating("food", "How would you rate the food at the school cafeteria?", "Horrible", "Fantastic")
survey.questions.append(rating1.toJson())

matrix1 = Matrix("moreOnFood", "How would you rate the food at the school cafeteria (in detail)?")
matrix1.columns = [{"value": 1, "text": "bad"},
                    {"value": 2, "text": "alright"},
                    {"value": 3, "text": "good"}]
matrix1.rows = [{"value": "appearance", "text": "food appearance"},
                    {"value": "taste", "text": "food taste"},
                    {"value": "price", "text": "food price"}]
survey.questions.append(matrix1.toJson())

comment1 = Comment("feedback", "Any advice to help us improve?")
survey.questions.append(comment1.toJson())

pipeline.append(survey.component)
```

#### main_loop.py

```python
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()
```

---


## Post Chat Survey

This page displays a survey immediately after a chatbot page. It will have the previous conversation shown directly above the survey. You can use it in a similar manner to the basic survey page above.

#### build.py

```python
# build.py

from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.post_chat_survey.post_chat_survey import PostChatSurvey

# ...

pipeline.append(Chatbot("Chat1").component)
pipeline.append(PostChatSurvey(title="A post chat survey", questions=[Text("overall", "How was the chatbot experience, overall?").toJson()]).component)
```

#### main_loop.py

```python
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()
```

---

## Compare Two Conversations

#### build.py
```python
# build.py

from components.compare.chats import CompareChatsSurvey

# ...

survey = CompareChatsSurvey("RandomComparison", text="My instructions here for the survey!")

survey.title = "Unique Survey Name here..."

text1 = Text("name", "What is your name?")
survey.questions.append(text1.toJson())

pipeline.append(survey.component)
```

#### main_loop.py
```python
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()

    if instruction == 'load_comparison':
        # Loads two conversations, and will display them side by side
        state.data["compare_bot_a"] = [{'id': 0, 'senderId': 'bot_a', 'text':"Hey how are you?"}, {'id': 1, 'senderId': 'bot_a', 'text':"Great thanks!"}]
        state.data["compare_bot_b"] = [{'id': 0, 'senderId': 'bot_b', 'text':"How's it going?"}]
```

---

## Compare Two Conversations and Choose One or the Other

#### build.py
```python
# build.py

from components.compare.chats import CompareChats

# ...

pipeline.append(CompareChats(identifier="UniqueIdentifierHere").component)
```

#### main_loop.py
```python
# main_loop.py

# ...

def update(state, instruction):

    # ...

    if instruction == 'advance':
        state.advance()

    if instruction == 'load_comparison':
        # Loads two conversations, and will display them side by side
        state.data["compare_bot_a"] = [{'id': 0, 'senderId': 'bot_a', 'text':"Hey how are you?"}, {'id': 1, 'senderId': 'bot_a', 'text':"Great thanks!"}]
        state.data["compare_bot_b"] = [{'id': 0, 'senderId': 'bot_b', 'text':"How's it going?"}]
```

---

> This page is still under construction ⚠️

---