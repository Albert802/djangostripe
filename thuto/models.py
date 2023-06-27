from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
class Grade(models.Model):
    GRADES =(('Grade 10','Grade 10'),('Grade 11','Grade 11'),('Grade 12','Grade 12'))
    grade = models.CharField(max_length=200,null=True,choices=GRADES)
    subject = models.ForeignKey(Subject,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.grade

class Lesson(models.Model):
    LANGUAGES = (
        ('English','English'),
        ('Sesotho', 'Sesotho'),
        ('IsiXhosa', 'IsiXhosa'),
        ('English and IsiXhosa', 'English and IsiXhosa'),
        ('English and Sesotho', 'English and Sesotho'),
        ('Sesotho, IsiXhosa and English', 'Sesotho, IsiXhosa and English'),
    )
    topic = models.CharField(max_length=200,null=True)
    subject = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade,null=True,on_delete=models.CASCADE)
    term =models.IntegerField(null=True,blank=True)
    languages = models.CharField(max_length=200,null=True,choices=LANGUAGES)
    video1 = models.FileField(blank=True,null=True)
    video2 = models.FileField(blank=True, null=True)
    video3 = models.FileField(blank=True, null=True)
    notes= models.FileField(blank=True, null=True)
    def __str__(self):
        return self.topic

class Exam(models.Model):
    lesson_title = models.ForeignKey(Lesson,blank=True,null=True,on_delete=models.CASCADE)
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 =models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)

    def __str__(self):

        return self.Corrans

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):

        return self.name