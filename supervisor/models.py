from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self, email, name=None, reg_no=None, hostel_no=None, room_no=None, mess_in=None, password=None):
        """
        Creates and saves a User with the given email, name, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            reg_no=reg_no,
            hostel_no=hostel_no,
            room_no=room_no,
            mess_in=mess_in,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name=None, reg_no=None, hostel_no=None, room_no=None, mess_in=None, password=None):
        """
        Creates and saves a staff user with the given email, name, and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            reg_no=reg_no,
            hostel_no=hostel_no,
            room_no=room_no,
            mess_in=mess_in,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name=None, reg_no=None, hostel_no=None, room_no=None, mess_in=None, password=None):
        """
        Creates and saves a superuser with the given email, name, and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            reg_no=reg_no,
            hostel_no=hostel_no,
            room_no=room_no,
            mess_in=mess_in,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50,null=True, blank=True)
    reg_no = models.PositiveIntegerField(null=True, blank=True)
    hostel_no = models.PositiveIntegerField(null=True, blank=True)
    room_no = models.CharField(max_length=10,null=True, blank=True)
    mess_in = models.BooleanField(default=False,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin



# class Supervisor(models.Model):
    
#     hostel_no = models.PositiveIntegerField()
#     def __str__(self):
#         return self.name

    
# class Student(CustomUser):
#     reg_no = models.PositiveIntegerField()
#     hostel_no = models.PositiveIntegerField()
#     room_no = models.CharField(max_length=10)
#     mess_in = models.BooleanField(default=False)
#     assigned_supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='students', null=True)

#     def __str__(self):
#         return f'Student: {self.name}'


class Meals(models.Model):
    meal_id = models.PositiveIntegerField(primary_key = True)
    main_dish = models.CharField(max_length = 100)
    roti = models.BooleanField(default=False) 
    side_dish = models.CharField(max_length = 100)

    def __str__(self):
        return f'Meal: {self.meal_id}'

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=10)
    breakfast = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='breakfast')
    lunch = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='lunch')
    dinner = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='dinner')

    def __str__(self):
        return f'Menu for {self.day}'
    
User = get_user_model()

class Fee(models.Model):
    fee_id = models.AutoField(primary_key=True)
    student_reg = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fees')
    in_date = models.DateField(null=True, blank=True)
    out_date = models.DateField(null=True, blank=True)
    fee_amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Fee {self.fee_id} for Student {self.student_reg.reg_no}"
    
    def update_fee_amount(self):
        if self.in_date and self.out_date:
            days_count = (self.out_date - self.in_date).days
            per_day_fee = 450
            additional_fee = days_count * per_day_fee
            self.fee_amount += additional_fee
            self.save()


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_text = models.TextField(null=True, blank=True)
    student_reg_no = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, choices=[
        ('poor', 'Poor'),
        ('neutral', 'Neutral'),
        ('good', 'Good'),
    ])

    def __str__(self):
        return f"Feedback ID: {self.feedback_id} - Student: {self.student_reg_no}"
