from django.shortcuts import render, redirect

def resume_selection(request):
    """Display available resume templates"""
    return render(request, 'resume_builder/resume_selection.html')

def resume_workspace(request, template_name):
    """Handle template selection and workspace initialization"""
    template_map = {
        'template1': 'resume_builder/resume_template1.html',
        'template2': 'resume_builder/resume_template2.html',
        'template3': 'resume_builder/resume_template3.html',
    }
    
    selected_template = template_map.get(
        template_name, 
        'resume_builder/template1_edit.html'
    )
    
    # Store selected template in session
    request.session['selected_template'] = selected_template
    request.session.modified = True
    
    return render(request, 'resume_builder/workspace.html', {
        'selected_template': selected_template
    })

def resume_preview(request):
    """Display resume preview"""
    selected_template = request.session.get(
        'selected_template', 
        'resume_builder/template1_edit.html'
    )
    return render(request, 'resume_builder/preview.html', {
        'selected_template': selected_template
    })