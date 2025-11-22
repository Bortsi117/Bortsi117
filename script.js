document.addEventListener('DOMContentLoaded', () => {
    const signUpButton = document.getElementById('signUpButton');
    const signInButton = document.getElementById('signInButton');
    const signInForm = document.getElementById('signIn');
    const signUpForm = document.getElementById('signUp');

    if (!signUpButton || !signInButton || !signInForm || !signUpForm) {
        console.warn('Missing expected elements', { signUpButton, signInButton, signInForm, signUpForm });
        return;
    }

    signUpButton.addEventListener('click', function () {
        signInForm.style.display = 'none';
        signUpForm.style.display = 'block';
    });

    signInButton.addEventListener('click', function () {
        signInForm.style.display = 'block';
        signUpForm.style.display = 'none';
    });
});