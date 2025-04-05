from django.shortcuts import render

# View for the resume selection page
def resume_selection(request):
    return render(request, 'resume_builder/resume_selection.html')


# View for the resume workspace with selected template
def resume_workspace(request, template_name):
    # Define allowed templates for security
    allowed_templates = {
        'template1': 'resume_builder/template1_edit.html',
        'template2': 'resume_builder/template2_edit.html',
        'template3': 'resume_builder/template3_edit.html',
    }

    # Fallback to template1 if invalid
    selected_template = allowed_templates.get(template_name, 'resume_builder/template1_edit.html')

    context = {
        'selected_template': selected_template
    }

    return render(request, 'resume_builder/workspace.html', context)

"""
def edit_resume(request, template_id):
    templates = {
        1: 'resume_builder/template1_edit.html',
        2: 'resume_builder/template2_edit.html',
        3: 'resume_builder/template3_edit.html'
    }
    
    template_file = templates.get(template_id, 'resume_builder/template1_edit.html')
    
    return render(request, template_file, {'template_id': template_id})

"""