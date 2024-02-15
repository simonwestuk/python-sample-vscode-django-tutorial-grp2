from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage
import datetime

class LogMessageTests(TestCase):

    def create_logmessage(self):
        """"
        Create a LogMessage instance
        """""
        return  LogMessage.objects.create(
            message="This is a test message.",
            log_date=timezone.now()
        )

    def test_logmessage_creation(self):
        """
        Test the creation of the LogMessage instance.
        """
        log_message = self.create_logmessage()
        self.assertTrue(isinstance(log_message, LogMessage))