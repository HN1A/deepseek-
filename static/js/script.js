// كود JavaScript لتحسين تجربة المستخدم

document.addEventListener('DOMContentLoaded', function() {
    // تحميل قائمة النماذج من الخادم
    fetch('/models')
        .then(response => response.json())
        .then(data => {
            const modelSelector = document.getElementById('model_name');
            if (modelSelector) {
                // حذف الخيارات الحالية
                modelSelector.innerHTML = '';
                
                // إضافة النماذج من البيانات المستلمة
                data.models.forEach(model => {
                    const option = document.createElement('option');
                    option.value = model.id;
                    option.textContent = `${model.name} - ${model.description}`;
                    modelSelector.appendChild(option);
                });
            }
        })
        .catch(error => console.error('Error loading models:', error));
    
    // تنفيذ التحقق من صحة النموذج قبل الإرسال
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const userInput = document.getElementById('user_input');
            if (!userInput.value.trim()) {
                event.preventDefault();
                alert('يرجى إدخال نص قبل الإرسال');
            }
        });
    }
});

