from django.db import models

class Teacher(models.Model):
    """
    Model Teacher.
    """
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    """
    Model Lesson. A teacher can only teach 1 lesson.
    """
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Student(models.Model):
    """
    Model Student.
    """
    name = models.CharField(max_length=250)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



