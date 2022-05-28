from sentences import *
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women", ]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past tense verbs.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a singular verb in past tense.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_verbs list.
        assert word in past_verbs

    # 2. Test the single present tense.

    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a singular verb in present tense.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_single_verbs list.
        assert word in present_single_verbs

    # 3. Test the plural present tense.

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a plural verb in present tense.
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_plural_verbs list.
        assert word in present_plural_verbs

    # 1. Test the future tense verbs.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think",
                    "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a verb in future tense.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_verbs list.
        assert word in future_verbs


def test_get_preposition():
    # 1. Test prepositions.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a single preposition.
        prepo = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert prepo in prepositions


def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # 1. Test the single determiners and nouns.

    single_determiners = ["a", "one", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman", ]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a list with 3 words(a preposition, a determiner and a noun).
        # then it gets splitted in 3 different variables.
        ginneaPig = get_prepositional_phrase(1).split(" ")
        prepo = ginneaPig[0]
        determ = ginneaPig[1]
        noun = ginneaPig[3]

        # Verify that the words from the get_prepositional_phrase function
        # are one of the words in their corresponding list.
        assert prepo in prepositions
        assert determ in single_determiners
        assert noun in single_nouns

    # 2. Test the plural determiners and nouns.

    plural_determiners = ["two", "some", "many", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women", ]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a list with 3 words(a preposition, a determiner and a noun).
        # then it gets splitted in 3 different variables.
        ginneaPig = get_prepositional_phrase(2).split(" ")
        prepo = ginneaPig[0]
        determ = ginneaPig[1]
        noun = ginneaPig[3]

        # Verify that the words from the get_prepositional_phrase function
        # are one of the words in their corresponding list.
        assert prepo in prepositions
        assert determ in plural_determiners
        assert noun in plural_nouns


def test_get_adjective():
    adjectives = ["flaky", "smoggy", "powerful", "panicky", "selfish",
                  "dusty", "truculent", "secret", "blushing", "elastic"]

    for _ in range(4):

        # Call the get_adjective function which
        # should return a single adjective.
        adjective = get_adjective()

        # Verify that the word returned from get_adjective
        # is one of the words in the adjectives list.
        assert adjective in adjectives


    # Call the main function that is part of pytest so that the
    # computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
