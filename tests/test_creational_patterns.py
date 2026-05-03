import unittest
import threading
from creational_patterns.simple_factory import DocumentFactory, Resume, CoverLetter
from creational_patterns.factory_method import LLMProcessor, OpenAIProcessor, GeminiProcessor
from creational_patterns.abstract_factory import ProfessionalPromptFactory, ProfessionalSystemPrompt, ProfessionalUserPrompt, CreativePromptFactory, CreativeSystemPrompt, CreativeUserPrompt
from creational_patterns.builder import CoverLetterBuilder
from creational_patterns.prototype import PromptCache
from creational_patterns.singleton import DatabaseConnection

class TestCreationalPatterns(unittest.TestCase):

    # 1. Simple Factory Tests
    def test_simple_factory_creation(self):
        doc1 = DocumentFactory.create_document("resume")
        doc2 = DocumentFactory.create_document("coverletter")
        self.assertIsInstance(doc1, Resume)
        self.assertIsInstance(doc2, CoverLetter)
        
    def test_simple_factory_edge_case(self):
        with self.assertRaises(ValueError):
            DocumentFactory.create_document("unknown_type")

    # 2. Factory Method Tests
    def test_factory_method(self):
        processor1 = OpenAIProcessor()
        processor2 = GeminiProcessor()
        self.assertIn("OpenAI", processor1.process_request("test"))
        self.assertIn("Gemini", processor2.process_request("test"))
        
        # Call the abstract method directly to cover the 'pass' statement
        LLMProcessor.process_request(None, "test")

    # 3. Abstract Factory Tests
    def test_abstract_factory(self):
        factory = ProfessionalPromptFactory()
        sys_prompt = factory.create_system_prompt()
        user_prompt = factory.create_user_prompt()
        self.assertIsInstance(sys_prompt, ProfessionalSystemPrompt)
        self.assertIsInstance(user_prompt, ProfessionalUserPrompt)
        
        creative_factory = CreativePromptFactory()
        creative_sys = creative_factory.create_system_prompt()
        creative_user = creative_factory.create_user_prompt()
        self.assertIsInstance(creative_sys, CreativeSystemPrompt)
        self.assertIsInstance(creative_user, CreativeUserPrompt)

    # 4. Builder Tests
    def test_builder_pattern(self):
        builder = CoverLetterBuilder()
        document = (builder
                    .add_contact_info("Jane Doe", "jane@example.com")
                    .add_body("I am writing to apply...")
                    .apply_tone("Enthusiastic")
                    .build())
                    
        self.assertEqual(document.contact_info, "Jane Doe | jane@example.com")
        self.assertEqual(document.tone, "Enthusiastic")
        self.assertTrue(len(document.body) > 0)

    # 5. Prototype Tests
    def test_prototype_cloning(self):
        cache = PromptCache()
        cache.load_cache()
        original = cache._cache['cover_letter_standard']
        clone = cache.get_prompt('cover_letter_standard')
        
        self.assertIsNot(original, clone) # Verify they are different objects in memory
        self.assertEqual(original.template, clone.template) # Verify attributes are the same

    # 6. Singleton Tests
    def test_singleton_thread_safety(self):
        instances = []
        
        def create_instance():
            instances.append(DatabaseConnection())
            
        threads = []
        for _ in range(10):
            t = threading.Thread(target=create_instance)
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
            
        # All 10 threads should return the exact same instance reference
        self.assertTrue(all(instance is instances[0] for instance in instances))