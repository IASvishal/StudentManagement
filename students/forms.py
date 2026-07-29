from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "roll_number": forms.NumberInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "course": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    # Validation methods should be here, not inside Meta

    def clean_name(self):
        name = self.cleaned_data["name"]

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only letters."
            )
        return name

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 16:
            raise forms.ValidationError(
                "Students must be at least 16 years old."
            )

        if age > 60:
            raise forms.ValidationError(
                "Age cannot exceed 60."
            )

        return age

    def clean_roll_number(self):
        roll = str(self.cleaned_data["roll_number"])

        if len(roll) != 9:
            raise forms.ValidationError(
                "Roll number should be exactly 9 digits."
            )

        return roll

