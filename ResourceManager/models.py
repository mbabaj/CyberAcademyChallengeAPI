from django.db import models

# Create your models here.
class Resource(models.Model):

    # Making category a selectable option makes it much easier to search by category
    CATEGORY_CHOICES = [
    ("network_security", "Network Security"),
    ("web_app_security", "Web Application Security"),
    ("cloud_security", "Cloud Security"),
    ("cryptography", "Cryptography"),
    ("digital_forensics", "Digital Forensics"),
    ("malware_analysis", "Malware Analysis"),
    ("penetration_testing", "Penetration Testing"),
    ("reverse_engineering", "Reverse Engineering"),
    ("incident_response", "Incident Response"),
    ("threat_intelligence", "Threat Intelligence"),
    ("compliance_governance", "Security Compliance & Governance"),
    ("secure_coding", "Secure Coding Practices"),
    ("identity_access", "Identity & Access Management"),
    ("security_awareness", "Security Awareness & Training"),
    ("red_team", "Red Teaming"),
    ("blue_team", "Blue Teaming"),
    ("purple_team", "Purple Teaming"),
    ("iot_security", "IoT Security"),
    ("mobile_security", "Mobile Security"),
    ("os_security", "Operating System Security"),
]
    
    title = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        max_length=5000,
        null=True,
        blank=True
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES
    )
    link = models.URLField(
        unique=True,
        help_text="Enter the full URL (e.g., https://example.com)",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name