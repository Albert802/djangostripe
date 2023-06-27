from django.shortcuts import render ,redirect
from .models import Subject,Lesson,Grade,Exam,Contact
from .filters import LessonFilter
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings # new
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from subscriptions.models import StripeCustomer
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    subject = Subject.objects.all()

    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object
        context = {
            'subscription': subscription,
            'product': product,
            'subject': subject

        }

        return render(request, 'thuto/index2.html',context )
    except StripeCustomer.DoesNotExist:

        return render(request, 'thuto/index2.html')


@login_required
def GradePage(request,pk):
    subject =Subject.objects.get(id=pk)
    grade = subject.lesson_set.all()

    my_filter = LessonFilter(request.GET, queryset=grade)
    grade =my_filter.qs

    context = {'grade':grade,'subject':subject,'my_filter':my_filter}
    return render(request, 'thuto/Grade2.html',context)
@login_required
def LessonPage(request,pk):
    lesson = Lesson.objects.get(id=pk)

    context = {'lesson':lesson}
    return render(request,'thuto/Lesson4.html',context)

@login_required
def examonline(request,pk):
    result = Lesson.objects.get(id=pk)
    results = result.exam_set.all()

    context={'results':results}
    return render(request,'thuto/index3.html',context)
@login_required
def news(request):
    context ={}
    return render(request,'thuto/news.html',context)
@login_required
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,'Thank you '+ str(name) +' for sending us a message we will take a look at!!!!')

            return redirect('thuto:contact')

    context ={'form':form}
    return render(request,'thuto/contact.html',context)


def visitor(request):
    context ={}
    return render(request,'thuto/visitor.html',context)

def login_demo(request):
    context= {}
    return render(request,'thuto/login_demo.html',context)

def register_demo(request):
    return render(request, 'thuto/signup.html')




