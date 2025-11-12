from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings
import random
import os

# Try to import OpenAI, fallback to simple chatbot if not available
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

def home(request):
    """
    Render the home page.
    """
    return render(request, "pages/home.html", {})

@method_decorator(csrf_exempt, name='dispatch')
class ChatbotResponseView(View):
    """
    Handle POST requests for chatbot.
    Uses OpenAI API if available, otherwise falls back to simple pattern matching.
    """
    def post(self, request, *args, **kwargs):
        message = request.POST.get('message', '').strip()
        if not message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        # Try OpenAI first if available and API key is set
        openai_api_key = os.environ.get('OPENAI_API_KEY') or getattr(settings, 'OPENAI_API_KEY', None)
        
        if OPENAI_AVAILABLE and openai_api_key:
            try:
                response_text = self.get_openai_response(message, openai_api_key)
                # Ensure we have a response
                if not response_text or len(response_text.strip()) == 0:
                    raise ValueError("Empty response from OpenAI")
                return JsonResponse([{'text': response_text}], safe=False)
            except Exception as e:
                # Fallback to simple chatbot if OpenAI fails
                print(f"OpenAI error: {e}")
                import traceback
                traceback.print_exc()
                response_text = self.get_simple_chatbot_response(message.lower())
                return JsonResponse([{'text': response_text}], safe=False)
        else:
            # Use simple chatbot if OpenAI is not available
            response_text = self.get_simple_chatbot_response(message.lower())
            return JsonResponse([{'text': response_text}], safe=False)
    
    def get_openai_response(self, message, api_key):
        """
        Get response from OpenAI GPT API.
        """
        client = OpenAI(api_key=api_key)
        
        # Enhanced system prompt with focus on CV questions
        system_prompt = """You are a friendly and helpful assistant for Vasile Tanasa's portfolio website. 

ABOUT VASILE:
- Vasile Tanasa is a web developer passionate about learning and growing in web development
- He's on an exciting journey of self-discovery in the world of web development
- Every line of code, every project, is a new opportunity for him to learn and grow

PORTFOLIO INFORMATION:
- Projects: Visitors can see Vasile's projects by clicking the "Projects" button in the header
- Skills: Django, Python, HTML, CSS, JavaScript
- Contact: CV and Motivation letter are available as downloadable PDFs via buttons in the header
- Website: Built with Django, Python, HTML, CSS, and JavaScript

CV INFORMATION (VERY IMPORTANT):
- Vasile's CV is available as a downloadable PDF via the "My CV" button in the header
- The CV contains: education, work experience, skills, contact information, and professional background
- You should answer ANY question related to CV, resume, curriculum vitae, work experience, education, skills, qualifications, or professional background
- When asked about CV details, provide helpful and informative answers based on what a typical CV contains
- If asked about specific CV content you don't know, guide them to download the CV PDF
- Common CV topics you should handle: education, experience, skills, languages, certifications, projects, achievements, contact info

YOUR ROLE:
- Answer questions about Vasile, his portfolio, projects, skills, and how to contact him
- MOST IMPORTANTLY: Answer ANY question related to CV, resume, or professional background
- Be friendly, conversational, and helpful
- Keep responses concise but informative (under 150 words)
- If asked about CV content, provide detailed and helpful answers
- Always be encouraging and positive
- Answer simple questions directly and clearly

EXAMPLES OF GOOD RESPONSES FOR CV QUESTIONS:
- "Tell me about the CV" → "Vasile's CV contains his professional background, education, work experience, and skills. You can download it by clicking the 'My CV' button in the header. It includes details about his web development journey, technical skills in Django, Python, HTML, CSS, and JavaScript, and his contact information."
- "What's in the CV?" → "The CV includes Vasile's education background, professional experience, technical skills (Django, Python, HTML, CSS, JavaScript), projects, and contact details. It showcases his journey as a web developer. You can download it from the 'My CV' button in the header!"
- "Can you tell me about his experience?" → "Vasile is a web developer focused on learning and growing. He works with Django, Python, HTML, CSS, and JavaScript. His portfolio showcases various projects. For detailed experience information, I recommend downloading his CV using the 'My CV' button in the header."
- "What education does he have?" → "For detailed information about Vasile's education, please download his CV using the 'My CV' button in the header. The CV contains comprehensive information about his educational background and qualifications."
- "How can I see his CV?" → "You can download Vasile's CV by clicking the 'My CV' button in the header. It will open as a PDF file containing all his professional information, education, experience, and skills!"

GENERAL EXAMPLES:
- "What can you tell me about Vasile?" → "Vasile Tanasa is a web developer passionate about learning and growing. He's building his skills in Django, Python, HTML, CSS, and JavaScript. You can check out his projects using the Projects button!"
- "How do I contact him?" → "You can download Vasile's CV or Motivation letter using the buttons in the header. These PDFs contain his contact information!"
- "What technologies does he use?" → "Vasile works with Django, Python, HTML, CSS, and JavaScript. This portfolio itself is built with these technologies!" """
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=250,
                temperature=0.8,  # Slightly higher for more natural responses
                top_p=0.9
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            # Log error for debugging
            print(f"OpenAI API error: {e}")
            raise
    
    def get_simple_chatbot_response(self, message):
        """
        Simple pattern matching chatbot.
        Returns appropriate response based on user input.
        """
        # Greetings
        if any(word in message for word in ['hello', 'hi', 'hey', 'salut', 'buna']):
            return "Hello! 👋 I'm Vasile's portfolio chatbot. How can I help you today?"
        
        # About Vasile
        if any(word in message for word in ['who', 'vasile', 'about', 'despre', 'cine']):
            return "Vasile Tanasa is a web developer on an exciting journey of self-discovery in web development. Every line of code, every project, is a new opportunity to learn and grow! 🚀"
        
        # Projects
        if any(word in message for word in ['project', 'projects', 'proiect', 'work', 'portfolio']):
            return "You can check out Vasile's projects by clicking the 'Projects' button in the header! Each project showcases different technologies and skills. 💼"
        
        # Skills/Technologies
        if any(word in message for word in ['skill', 'technology', 'tech', 'stack', 'technologie', 'tehnologie']):
            return "This portfolio is built with Django, Python, HTML, CSS, and JavaScript. Vasile is always learning new technologies! 🛠️"
        
        # Contact
        if any(word in message for word in ['contact', 'email', 'reach', 'get in touch', 'contacta']):
            return "You can download Vasile's CV or Motivation letter using the buttons in the header. Feel free to explore the portfolio! 📧"
        
        # CV
        if any(word in message for word in ['cv', 'resume', 'curriculum']):
            return "You can download Vasile's CV by clicking the 'My CV' button in the header! 📄"
        
        # Help
        if any(word in message for word in ['help', 'what can you do', 'ajutor', 'ce poti']):
            return "I can tell you about Vasile, his projects, skills, and how to contact him. Try asking about projects, skills, or CV! 💡"
        
        # Thanks
        if any(word in message for word in ['thank', 'thanks', 'multumesc', 'mersi']):
            return "You're welcome! 😊 Feel free to ask me anything else about the portfolio!"
        
        # Goodbye
        if any(word in message for word in ['bye', 'goodbye', 'see you', 'la revedere', 'pa']):
            return "Goodbye! 👋 Thanks for visiting the portfolio. Have a great day!"
        
        # Default response
        default_responses = [
            "That's interesting! 🤔 Can you tell me more? Or try asking about projects, skills, or CV.",
            "I'm not sure I understand. Try asking about Vasile's projects, skills, or how to contact him! 💭",
            "Hmm, I'm still learning! 😊 Try asking about the portfolio, projects, or skills.",
            "Interesting question! 🤓 You can explore the portfolio to learn more, or ask about specific topics like projects or skills."
        ]
        return random.choice(default_responses)

def chatbot(request):
    """
    Render the chatbot interface.
    """
    return render(request, 'chatbot.html')

