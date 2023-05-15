from django.shortcuts import render
from django.views import generic
from .models import Booking


def booking(request):
    """
    To display the booking form so the user can book a room.
    """
    return render(request, 'booking/booking.html')

# def booking(request):
#     """
#     To display the booking form so the user can book a room.
#     They get a message if their enetered booking has already been booked.
#     They get an email for confirmation.
#     """
#     form = BookingForm()
#     booked = False
#     error = None
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         booking = form.save(commit=False)
#         # booking can be made: save & send email
#         if form.is_valid():
#             # checks for double booking
#             if not booking.is_time_taken():
#                 booking.user = request.user
#                 booking.save()
#                 booked = True
#                 email_to = booking.email
#                 subject = 'Your booking'
#                 message = f'Hi {booking.first_name},\n\n\
#                         Your booking has been placed:\n\n\
#                         DATE:{booking.date}\n\
#                         ROOM:{booking.room_name}\n\
#                         TIME:{booking.time}\n\
#                         We look forward to seeing you!'
#                 email_from = 'theescaperoomldn@gmail.com'
#                 recipient_list = [email_to, ]
#                 send_mail(subject, message, email_from, recipient_list)
#             # error message for double booking
#             else:
#                 error = "This slot is not available"

#     context = {
#         'form': form,
#         'booked': booked,
#         "error": error
#         }

#     return render(request, 'book.html', context)

