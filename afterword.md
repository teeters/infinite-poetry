## Afterword

The Free Infinite Poetry Generator began as a writing prompt, in which we were asked to write six words, free-associate based on each word, and use the resulting words to write a poem. In its current form, the project is a meditation on the use and marketing of large language models or LLMs.

Currently, many LLM services--such as chatting or writing poetry--are offered for "free." This word suggests two things: one, that our usage of these technologies is unrestricted; and two, that there is no cost associated with them. In reality, neither of these things is true. LLMs take massive amounts of electricity and human labor to build and operate, and our usage of them is subject to extensive limitation and monitoring.

Users of the Free Infinite Poetry Generator will quickly notice a couple of caveats. One is that the phrase "barbed wire" will almost always appear in the poem generated, no matter what the user inputs or how strongly they urge the model not to mention it. The other is that some words are omitted from the poems generated, and the amount increases by 5% every time the generator is run. The intended effect is that the reader becomes aware that their experience is being manipulated, and that it depends on a finite resource. Every time they answer yes to the question, "Do you wish to continue?", something is used up.

Technically savvy users will note that both these constraints are fairly easy to get around by modifying the program's hidden files, but this is little different from the ways that software companies constrain their users' experiences by hiding the controls. Apathy and incuriosity are as much a part of the trap as the software.

Finally, the main loop of this program is designed to be readable as a standalone poem. It is as follows:

```
while True:
        seeds = get_seeds()
        advice = get_advice()
        forced = get_forced()
        
        say("Free associating...\n")
        words = free_associate(seeds)

        say("Writing poem...\n")
        poem = get_poem(words, advice, forced)
        poem = decay(poem, forced, age)
        say(poem)
        age = increase_age(age)
        print()

        if should_break():
            break
        else:
            print()
            continue
```
