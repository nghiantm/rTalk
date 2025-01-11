# Real Talk

## Inspiration
Multilingualism is one of the best tools that someone can have. It allows humans to join in and become something much larger than us. Whether it be conversing with world leaders or simply wanting to talk to a new friend, everyone can benefit from knowing a foreign language. That is why, during the last 20 years, almost all countries have published a curriculum for at least one foreign language. However, these learning methods rely on repetitive exercises and often overlook verbal skills, a key indicator of the ability to speak with others.

As someone who grew up in Vietnam and has been around many immigrants, we have seen many complicated situations that result from a lack of language. For example, someone in a life-threatening condition may not be able to communicate with doctors. Even with children of this generation, who benefit from the new curriculum, most, if not all, could not demonstrate spoken proficiency and cultural awareness outside a classroom.

This information gave us the inspiration for **Real Talk**. We want it to be a convenient app that everyone can access. Real Talk will enable you to practice your verbal skills anywhere, offering personalization and multiple languages.

## What It Does
Real Talk is a personalized AI chatbot (or speakbot, to be more accurate) that can assess your skill level.

You will be able to talk about whatever you want. Through a simple user interface, you can have a conversation that provides real-time catered feedback. The vibe and feedback are tailored to your learning goal (e.g., office work, traveling). The difficulty is also constantly adapted to your level.

## How We Built It
We used a combination of many technologies and AI models to make Real Talk:

- **Dictation and Text-to-Speech**: Implemented using a wrapper on SpeechRecognition.
- **AI Language Models**: Leveraged NousResearch/Nous-Hermes-2-Yi-34B hosted on Together.AI to generate AI agent responses.
- **Data Storage**: Used MongoDB Atlas and Express.js. MongoDB's blazing-fast response time allows us to make the conversation even more real-time.
- **Proficiency Level Classification**: Trained a text classifier model with scikit-learn. We generated a training dataset corresponding to ACTFL Proficiency Guidelines 2024. Running on a Flask microservice, this model helps us visualize the user's improvements.

## Challenges We Ran Into

### Dictation and Text-to-Speech
Our major challenge was figuring out the dictation and text-to-speech. Initially, we planned to use an external API, but it cost too much and was hard to configure. As a result, we compromised with React packages to address this issue.

### Measuring Fluency
Another challenge was determining how to measure the user's fluency level. We eventually decided to use qualitative feedback based on ACTFL guidelines. The scoring is based on the average ACTFL score of the five most recent responses provided. This approach ensures that speaking frequently does not negatively impact the scoring system.

---

Real Talk makes language learning accessible, adaptable, and interactive. We aim to help users enhance their verbal communication skills and gain cultural awareness, bridging the gap between theoretical learning and real-world application.
