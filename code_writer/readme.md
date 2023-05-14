# Purpose
The goal of this project is to create a private model that is really effective at writing code.

# High Level Design
Definitions:
MANN - Memory Augmented Nueral Network
Reinforcement learning - learn live in the environment
Generative Adversarial Networks - generative network creates solutions and the discrimitive network generators validators


Psuedo Code:
For each desired language to support:
    Try custom models, existing language models. For each set:
        1. Traditional training of generative network - get sets of problem descriptions and solutions (manual, web scraping, auto generated)
        2. Traditional training of discrimitive network - get sets of problem descriptions and associated unittests (manual, web scraping, auto generated)
        3. create value function around test coverage and all tests passing
        4. if value function is good take opportunity to review network traffic and prune unused routes but introduce random connections
        5. Take original prompts and run networks against each other until all cases pass with the desired code coverage
        6. Repeat steps 1 - 2 with a supervised code review step to improve quality



Ideas
1. internet search augmented NN. enable ability to search internet, detect code blocks from results, detect API docs, and use to create contextually relevant set of likely next words and their probability
2. local search augemented NN. enable ability to search local database of content (ie filtered set of search results, all pypi content)
3. build initial training dataset using package repositories (get package documentation, source code, and test files)
4. live monitor a network's traffic on positive results and use to destroy edges and randomly introduce new connections and weights (over time reduce the likelihood of generating a new weight)
5.

