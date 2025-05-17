from django.db import models


class User(models.Model):
    PROGRAM_CHOICES = [
        ('basic', 'Basic'),
        ('advanced', 'Advanced'),
        ('pro', 'Pro'),
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    program = models.CharField(max_length=100, choices=PROGRAM_CHOICES)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Fragment(models.Model):
    COMPLEXITY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    content = models.TextField()
    complexity_level = models.CharField(max_length=50, choices=COMPLEXITY_CHOICES)
    theme = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'Fragment {self.id} - {self.theme}'


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fragment = models.ForeignKey(Fragment, on_delete=models.CASCADE)
    test_date = models.DateTimeField(auto_now_add=True)
    reading_speed = models.PositiveIntegerField()  # слов/мин
    comprehension = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # проценты
    session_data = models.JSONField()

    def __str__(self):
        return f'Result for {self.user} on {self.test_date}'
