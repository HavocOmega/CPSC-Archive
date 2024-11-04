import unittest
from support_functions import full_word


class TestFullWordFunction(unittest.TestCase):
    # Basic tests for exact word matches
    def test_exact_match_start(self):
        self.assertTrue(full_word("Hello world!", "Hello"), "Basic test for exact match at start")

    def test_exact_match_end(self):
        self.assertTrue(full_word("Hello world!", "world"), "Basic test for exact match at end")

    def test_case_insensitive_match(self):
        self.assertTrue(full_word("Hello world!", "hello"), "Case-insensitive check for 'hello'")

    # Word not present
    def test_word_not_in_sentence_1(self):
        self.assertFalse(full_word("Hello world!", "goodbye"), "Word 'goodbye' is not in the sentence")

    def test_word_not_in_sentence_2(self):
        self.assertFalse(full_word("The sky is blue", "green"), "Word 'green' is not in the sentence")

    # Word at the beginning or end of the sentence
    def test_word_at_start(self):
        self.assertTrue(full_word("hello world!", "hello"), "Word 'hello' at the start")

    def test_word_at_end(self):
        self.assertTrue(full_word("hello world!", "world"), "Word 'world' at the end")

    def test_word_in_middle(self):
        self.assertTrue(full_word("oh hi there", "hi"), "Word 'hi' in the middle of the sentence")

    # Word with punctuation around it
    def test_word_with_exact_punctuation_match(self):
        self.assertTrue(full_word("Hi there, chat,231!", "chat,231"), "Exact match for 'chat,231'")

    def test_partial_match_with_punctuation(self):
        self.assertTrue(full_word("Hi there, chat,231!", "chat"), "Partial match for 'chat' in 'chat,231'")

    # Word containing punctuation but should still match
    def test_word_with_punctuation_1(self):
        self.assertTrue(full_word("Hello, friend!", "Hello,"), "Word with punctuation 'Hello,'")

    def test_word_with_punctuation_2(self):
        self.assertTrue(full_word("The answer is: 42.", "42."), "Number with punctuation '42.'")

    # Subword match
    def test_subword_in_word_1(self):
        self.assertFalse(full_word("This is a high tower", "hi"), "'hi' is part of 'high', not a separate word")

    def test_subword_in_word_2(self):
        self.assertFalse(full_word("Testing chat231", "chat"), "'chat' is part of 'chat231'")

    def test_subword_in_word_3(self):
        self.assertFalse(full_word("The password is abc123", "abc"), "'abc' is part of 'abc123'")

    # Words with punctuation at the start/end
    def test_word_with_punctuation_at_start(self):
        self.assertTrue(full_word("Wow! What a test!", "Wow!"), "Word 'Wow!' with exclamation")

    def test_word_with_punctuation_at_end(self):
        self.assertTrue(full_word("End of sentence.", "sentence."), "Word 'sentence.' at the end")

    def test_special_character_in_word_1(self):
        self.assertTrue(full_word("Email: someone@test.com", "test.com"), "Word with special characters 'test.com'")

    def test_special_character_in_word_2(self):
        self.assertFalse(full_word("Email: someone@test.com", "@test.com"), "'@test.com' is attached to someone")

    def test_special_character_in_word_3(self):
        self.assertTrue(full_word("Insta: @don.withyou", "@don.withyou"), "Word with special characters '@don.withyou'")

    def test_special_character_in_word_4(self):
        self.assertTrue(full_word("Insta: @don.withyou", "@don"), "Word with special characters '@don' not attached")

    # Sentence with multiple punctuations
    def test_multiple_punctuations_1(self):
        self.assertTrue(full_word("Hi, there! Let's chat:231.", "chat:231"), "Word with colon 'chat:231'")

    def test_multiple_punctuations_2(self):
        self.assertTrue(full_word("Hi, there! Let's chat:231.", "chat"), "Partial word 'chat' from 'chat:231'")

    # Testing empty word or sentence
    def test_empty_sentence(self):
        self.assertFalse(full_word("", "test"), "Empty sentence should return False")

    def test_empty_word(self):
        self.assertFalse(full_word("hello world", ""), "Empty word should return False")

    def test_both_empty(self):
        self.assertFalse(full_word("", ""), "Both sentence and word empty")

    # Number as word
    def test_exact_number_match(self):
        self.assertTrue(full_word("The number is 12345.", "12345"), "Exact number match '12345'")

    def test_partial_number_match(self):
        self.assertFalse(full_word("The number is 12345.", "12"), "'12' is part of '12345', not a full word")

    # Words with hyphen
    def test_word_with_hyphen(self):
        self.assertTrue(full_word("Well-written essay", "Well-written"), "Word with hyphen 'Well-written'")

    def test_partial_word_with_hyphen(self):
        self.assertTrue(full_word("Well-written essay", "written"),
                        "'written' is part of 'Well-written' but not separated by the symbol")

    # Handling multiple words and punctuation
    def test_multiple_words_with_punctuation_1(self):
        self.assertTrue(full_word("First, second, and third!", "first"), "Word 'first' with punctuation")

    def test_multiple_words_with_punctuation_2(self):
        self.assertTrue(full_word("First, second, and third!", "second"), "Word 'second' in the middle")

    def test_multiple_words_with_punctuation_3(self):
        self.assertTrue(full_word("First, second, and third!", "third"), "Word 'third' with exclamation at end")

    # Case with symbols around the word
    def test_word_with_symbols_1(self):
        self.assertTrue(full_word("Welcome to $ChatBot#231", "ChatBot#231"),
                        "Word with special characters '$ChatBot#231'")

    def test_word_with_symbols_2(self):
        self.assertTrue(full_word("Hello there@home", "there@home"), "Word with '@' symbol 'there@home'")

    def test_word_with_symbols_3(self):
        self.assertTrue(full_word("Check this out: chat@231!", "chat@231"), "Word with special characters 'chat@231'")

    def test_word_with_symbols_4(self):
        self.assertTrue(full_word("Check this out: !@*($)!Chat@@$@!31!!#@$", "chat@@$@"),
                        "Word with special characters 'chat@@$@'")

    def test_word_with_symbols_5(self):
        self.assertTrue(full_word("Check this out: !@*($)!Chat@@$@!31!!#@$", "31"), "Word with special characters '31'")

    def test_word_with_symbols_6(self):
        self.assertTrue(full_word("Check this out: !@*($)!Chat@@$@!31!!#@$", "chat"),
                        "Word with special characters 'chat'")

    # Edge cases with minimal sentences
    def test_single_letter_match(self):
        self.assertTrue(full_word("a", "a"), "Single letter match")

    def test_single_letter_mismatch(self):
        self.assertFalse(full_word("a", "b"), "Single letter mismatch")

    def test_empty_word_in_single_letter_sentence(self):
        self.assertFalse(full_word("a", ""), "Empty word in single-letter sentence")

    # Word inside symbols
    def test_word_inside_symbols_1(self):
        self.assertTrue(full_word("Let's test some-cases", "some-cases"), "Word with hyphen 'some-cases'")

    def test_partial_word_inside_symbols(self):
        self.assertTrue(full_word("Let's test some-cases", "some"), "Partial word 'some' from 'some-cases'")

    # Case sensitivity checks
    def test_case_insensitive_1(self):
        self.assertTrue(full_word("HELLO world!", "hello"), "Case-insensitive match for 'hello'")

    def test_case_insensitive_2(self):
        self.assertTrue(full_word("HELLO world!", "WORLD"), "Case-insensitive match for 'WORLD'")

    def test_case_insensitive_3(self):
        self.assertTrue(full_word("Python is cool!", "PYTHON"), "Case-insensitive match for 'PYTHON'")

    # Complex test cases with symbols
    def test_complex_case_symbols_1(self):
        self.assertTrue(full_word("Hi! You, Chat-231 and Chat$231; are all invited.", "Chat-231"),
                        "Word with hyphen 'Chat-231'")

    def test_complex_case_symbols_2(self):
        self.assertTrue(full_word("Hi! You, Chat-231 and Chat$231; are all invited.", "Chat$231"),
                        "Word with dollar sign 'Chat$231'")

    def test_partial_complex_case_symbols_1(self):
        self.assertTrue(full_word("Hi! You, Chat-231 and Chat$231; are all invited.", "Chat"),
                        "Partial match for 'Chat'")

    def test_partial_complex_case_symbols_2(self):
        self.assertTrue(full_word("Hi! You, Chat-231 and Chat$231; are all invited.", "231"),
                        "'231' is separated from Chat-231 by a symbol")

if __name__ == "__main__":
    unittest.main()