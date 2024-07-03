from django.shortcuts import render, redirect
from supervisor.models import Menu, Fee, User, Feedback
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from datetime import date

User = get_user_model()

def loginStudent(request):
    if request.method == "POST":
        email = request.POST.get('email_st')
        password = request.POST.get('password_st')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            fee = Fee.objects.get_or_create(student_reg=user)[0]
            menus = Menu.objects.all()
            request.session['user_id'] = user.id

            context = {
                'menus': menus,
                'fee': fee,
                'student': user
            }

            return render(request, 'student/index.html', context)  # Redirect to the student index URL
        else:
            messages.error(request, "Wrong credentials")
            return render(request, "student/login_student.html", {'error': "Wrong credentials"})

    return render(request, "student/login_student.html")

def index(request):
    user_id = request.session.get('user_id')
    student = User.objects.get(pk=user_id)
    fee = Fee.objects.get_or_create(student_reg=student)[0]
    menus = Menu.objects.all()

    if request.method == "POST" and 'toggle_mess_in' in request.POST:
        if student.mess_in:
            fee.out_date = date.today()
        else:
            fee.in_date = date.today()

        student.mess_in = not student.mess_in
        fee.update_fee_amount()
        student.save()
        fee.save()

    context = {
        'menus': menus,
        'fee': fee,
        'student': student
    }
    return render(request, 'student/index.html', context)

def submit_feedback(request):
    if request.method == 'POST':
        student_reg_no = request.POST.get('student_reg_no')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')

        #getting student_reg_no_id from User model for the student_reg_no
        student_id = User.objects.get(reg_no = student_reg_no).id

        # Save feedback to database
        feedback = Feedback.objects.create(
            student_reg_no_id=student_id,
            feedback_text=feedback_text,
            rating=rating
        )
        feedback.save()

        messages.success(request, 'Feedback submitted successfully.')
        return redirect('index_student') 

    return render(request, 'student/index.html')  

