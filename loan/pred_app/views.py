from django.shortcuts import render,redirect
import pickle
pickled_model = pickle.load(open('./pred_app/logreg_model.pkl', 'rb'))
def home(request):
    
    context = {}
    return render(request, 'pred_app/home.html', context)

def result(request):
    status = ''
    if request.method=='POST':
        gender = int( request.POST.get('gender') )
        married = int( request.POST.get('married') )
        dependents = int( request.POST.get('dependents') )
        education = int( request.POST.get('education') )
        employment = int( request.POST.get('employment') )
        income = float (request.POST.get('income'))
        co_income = float (request.POST.get('co_income'))
        loan_amount = float (request.POST.get('loan_amount'))
        l_term = float (request.POST.get('l_term'))
        cr_history = float (request.POST.get('cr_history'))
        p_area = int( request.POST.get('p_area') )
        total_income = float ( request.POST.get('total_income') )
        print(gender,married,dependents,education,employment,income,co_income,loan_amount,l_term,cr_history,p_area,total_income)
        print('=========', type(gender), type(married),type(dependents),type(education))
        data = [ [gender,married,dependents,education,employment,income,co_income,loan_amount,l_term,cr_history,p_area,total_income ] ]
        result = pickled_model.predict(data)
        print('=======result: ',result)
        if result[0]==1:
            status = "Eligible For The Loan"
        else:
            status = "Not Eligible For The Loan"
    context = {'status': status}
    return render(request, 'pred_app/result.html', context)