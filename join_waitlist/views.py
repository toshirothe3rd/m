from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import WaitlistEntry

def join_waitlist(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required.'}, status=400)
        
        # Check if email already exists in the waitlist
        if WaitlistEntry.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'This email is already on the waitlist.'}, status=400)
        
        # Save the email to the database
        WaitlistEntry.objects.create(email=email)
        
        # Email template
        email_html_message = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to the Medit AI Waitlist!</title>
    <!--[if mso]>
    <noscript>
    <xml>
        <o:OfficeDocumentSettings>
            <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    </noscript>
    <![endif]-->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { -ms-interpolation-mode: bicubic; }
        img { border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
        table { border-collapse: collapse !important; }
        body { height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important; }
        a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; }
        @media screen and (max-width: 525px) {
            .wrapper { width: 100% !important; max-width: 100% !important; }
            .responsive-table { width: 100% !important; }
            .padding { padding: 10px 5% 15px 5% !important; }
            .section-padding { padding: 0 15px 50px 15px !important; }
            .mobile-button-container { margin: 0 auto; width: 100% !important; }
            .mobile-button { padding: 15px !important; border: 0 !important; font-size: 16px !important; display: block !important; }
        }
        .social-icon {
            display: inline-block;
            margin: 0 5px;
            width: 35px;
            height: 35px;
        }
    </style>
</head>
<body style="margin: 0 !important; padding: 0 !important; background-color: #F4F7FA;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td bgcolor="#F4F7FA" align="center" style="padding: 50px 10px 0 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;" class="responsive-table">
                    <tr>
                        <td>
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td>
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td style="padding: 0 0 0 0; font-size: 16px; line-height: 25px; color: #232323; font-family: 'Inter', Helvetica, Arial, sans-serif;" class="padding">
                                                    <h2 style="font-size: 28px; font-weight: 700; line-height: 36px; color: #19469D; margin: 0;">Welcome to the Medit AI Waitlist!</h2>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; color: #232323; font-family: 'Inter', Helvetica, Arial, sans-serif;" class="padding">
                                                    Thank you for joining our waitlist. We're thrilled to have you on board as we prepare to revolutionize medical writing with AI.
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; color: #232323; font-family: 'Inter', Helvetica, Arial, sans-serif;" class="padding">
                                                    Here's what you can expect:
                                                    <ul>
                                                        <li>Early access to our platform</li>
                                                        <li>Exclusive updates on our progress</li>
                                                        <li>Special launch offers for waitlist members</li>
                                                    </ul>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="center">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                        <tr>
                                                            <td align="center" style="padding: 30px 0 0 0;" class="padding">
                                                                <table border="0" cellspacing="0" cellpadding="0" class="mobile-button-container">
                                                                    <tr>
                                                                        <td align="center" style="border-radius: 8px;" bgcolor="#19469D"><a href="https://meditai.up.railway.app/join-waitlist" target="_blank" style="font-size: 16px; font-family: 'Inter', Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; border-radius: 8px; padding: 15px 25px; border: 1px solid #19469D; display: inline-block;" class="mobile-button">Visit Our Website</a></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 30px 0 0 0; font-size: 16px; line-height: 25px; color: #232323; font-family: 'Inter', Helvetica, Arial, sans-serif;" class="padding">
                                                    If you have any questions or feedback, don't hesitate to reach out. We're here to help!
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; color: #232323; font-family: 'Inter', Helvetica, Arial, sans-serif;" class="padding">
                                                    Best regards,<br>
                                                    The Medit AI Team
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#F4F7FA" align="center" style="padding: 30px 10px 0 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;" class="responsive-table">
                    <tr>
                        <td style="padding: 30px 0 30px 0; border-top: 1px solid #DDDDDD;" align="center">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td align="center" style="padding: 20px 0 0 0;">
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td align="center" style="font-family: 'Inter', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; color: #666666;">
                                                    <span style="font-family: 'Inter', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; color: #666666;">Copyright &copy; 2025 Medit AI. All Rights Reserved.</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
        '''
        
        # Send confirmation email
        send_mail(
            'Thank you for joining the waitlist',  # Subject
            '',  # Plain text body (optional)
            settings.DEFAULT_FROM_EMAIL,  # From email
            [email],  # To email
            fail_silently=False,
            html_message=email_html_message  # HTML content
        )
        
        # Return JSON response
        return JsonResponse({'success': True, 'message': 'Thank you for joining our waitlist! Confirmation email sent.'}, status=200)
    
    # For GET requests, render the index.html page
    return render(request, 'join_waitlist/index.html')
