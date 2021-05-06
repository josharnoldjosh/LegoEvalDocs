# build.py

The `build.py` file is where a lot of the magic happens in LegoEVAL. In this guide, we will talk a bit about how to use the `build.py` file.


#### 1. Import Your Pages

We've already built a solid library of pages for you to use in the **Page Library** section of the documentation. We've taken the liberty of importing these pages for you at the top of the `build.py` file like so:

```python
# ...

from components.page.page import Page as Instruction
from components.load_mturk.load_mturk import LoadMTurk
from components.submit_mturk.submit_mturk import SubmitMTurk
from components.survey.survey import Survey, RadioGroup, CheckBox, Text, Rating, Matrix, Comment
from components.chatbot.chatbot import Chatbot
from components.compare.chats import CompareChats
from components.compare.chats_survey import CompareChatsSurvey
from components.post_chat_survey.post_chat_survey import PostChatSurvey

# ...
```

> Notice all of the pages are found in the `components` folder of `LegoEVAL`, in case you're interested in looking at the source files.

If you have a custom page you've created, you'll want to import it here like so, too.


#### 2. Read Some Documentation

For each pre-built page, you can find detailed documentation for that component in the **Page Library** section of our docs. 


#### 3. Add Your Pages

Once you've imported your pages and read-up on the documentation, you can then begin to construct your `build.py`. We've got an example below for you:

```python

# ...

### ~~~ Build Your Task Below ~~~ ###

# A Page that displays a title, description, and button
pipeline.append(
    Instruction(
        title="Welcome to this demo task!",
        description="Here is a description.",
        button="Click me to Start the Task"
    )
    .component
)

# A Survey Page
survey = Survey("survey_1")
survey.title = "Task Survey"
survey.questions.append(Comment("comment", "Please type a breif comment here.").toJson())
pipeline.append(survey.component)

### ~~~ End of Your Task ~~~ ###

# ...

```

You can see we've created a task with two different pages. The first page is a simple [Instruction Page](/temp) that displays a title and description. The next is a [Survey Page](/temp) that presents a survey to the user.

The survey page has a lot of customization, you can add different questions in different orders, etc.


#### 4. A Few Notes

It's that easy to snap together pages to build your task. Our whole goal with the LegoEVAL framework is to make designing a crowd-sourced task easy.

There are **two important notes** that you should be aware of:

1. To define any "backend" logic for each page, you'll need to lastly edit the `main_loop.py` file. Details can be found [here](/temp).
2. If you need to customize the logic of a page, or build your own page that isn't currently supported, you can find out how to do that [here](/temp).


---