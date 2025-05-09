import os
import json
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# تحميل متغيرات البيئة من الملف .env
load_dotenv()

app = Flask(__name__)

# الحصول على مفتاح API من المتغيرات البيئية
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

@app.route('/')
def index():
    """عرض الصفحة الرئيسية"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    """استقبال الطلب وإرسال استعلام إلى DeepSeek API"""
    try:
        # الحصول على المدخلات من النموذج
        user_input = request.form.get('user_input')
        model_name = request.form.get('model_name', 'deepseek-chat')  # استخدم DeepSeek-V3 افتراضياً
        
        # تحضير العنوان وترويسة الطلب
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        # تحضير محتوى الطلب
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": "أنت مساعد ذكي ومفيد."},
                {"role": "user", "content": user_input}
            ],
            "stream": False  # تعيين stream إلى False للحصول على استجابة كاملة بدلاً من تدفق
        }
        
        # إرسال الطلب إلى DeepSeek API
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        
        # التحقق من استجابة الخادم
        if response.status_code == 200:
            # استخراج النص من الاستجابة
            result = response.json()
            generated_text = result['choices'][0]['message']['content']
            
            # إرجاع النتيجة
            return render_template('result.html', 
                                  user_input=user_input,
                                  generated_text=generated_text,
                                  model_name=model_name)
        else:
            # إرجاع رسالة خطأ إذا فشل الطلب
            return jsonify({"error": f"Error from DeepSeek API: {response.text}"}), 500
    
    except Exception as e:
        # التعامل مع الأخطاء الأخرى
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """واجهة برمجة تطبيقات JSON للتكامل مع تطبيقات أخرى"""
    try:
        data = request.get_json()
        user_input = data.get('user_input')
        model_name = data.get('model_name', 'deepseek-chat')
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": "أنت مساعد ذكي ومفيد."},
                {"role": "user", "content": user_input}
            ],
            "stream": False
        }
        
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            generated_text = result['choices'][0]['message']['content']
            return jsonify({
                "success": True,
                "generated_text": generated_text,
                "model_name": model_name
            })
        else:
            return jsonify({
                "success": False,
                "error": f"Error from DeepSeek API: {response.text}"
            }), 500
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An error occurred: {str(e)}"
        }), 500

@app.route('/models')
def list_models():
    """عرض قائمة النماذج المتاحة من DeepSeek"""
    models = [
        {"id": "deepseek-chat", "name": "DeepSeek-V3", "description": "أحدث نموذج محادثة متقدم من DeepSeek"},
        {"id": "deepseek-reasoner", "name": "DeepSeek-R1", "description": "نموذج التفكير المنطقي من DeepSeek"}
    ]
    return jsonify({"models": models})

if __name__ == '__main__':
    app.run(debug=True)
