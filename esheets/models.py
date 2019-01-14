from django.db import models


class Test(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    test_name = models.CharField(max_length=32)

    def __str__(self):
        return self.test_name


class Student(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentTest(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='studenttest', on_delete=models.CASCADE)

    def __str__(self):
        return self.test.test_name + " - " + self.owner.name


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=256)

    def __str__(self):
        return self.test.test_name + " | " + self.question


class StudentResponse(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_test = models.ForeignKey(StudentTest, related_name='student_response', on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    def __str__(self):
        return self.question.question + ' | ' + self.answer


class StudentAnswerPoints(models.Model):
    student_response = models.ForeignKey(StudentResponse, on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.points


class StudentTestGrade(models.Model):
    grade = models.IntegerField(blank=True, null=True)
    student_test = models.OneToOneField(StudentTest, on_delete=models.CASCADE)

    def __str__(self):
        return self.grade
