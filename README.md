

# DeepSeek AI App

تطبيق ذكاء اصطناعي يعتمد على نموذج DeepSeek، تم تطويره باستخدام Flask في لغة Python.

## المتطلبات الأساسية

- Python 3.8 أو أحدث
- بيئة افتراضية (Virtual Environment)
- مفتاح API من منصة DeepSeek
- مكتبات Python التالية:
  - flask
  - requests
  - python-dotenv

---

## خطوات إعداد المشروع

### 1. إنشاء بيئة افتراضية

استخدم الأمر التالي لإنشاء بيئة افتراضية جديدة باسم `deepseek-env`:

```bash
python3 -m venv deepseek-env

2. تفعيل البيئة الافتراضية

إذا كنت تستخدم نظام لينكس أو ماك:

source deepseek-env/bin/activate

إذا كنت تستخدم نظام ويندوز:

deepseek-env\Scripts\activate


---

3. تثبيت المكتبات المطلوبة

بعد تفعيل البيئة الافتراضية، نفّذ الأمر التالي لتثبيت الحزم:

pip install flask requests python-dotenv


---

4. إعداد مفتاح API

قم بإنشاء ملف باسم .env في مجلد المشروع الرئيسي، ثم أضف السطر التالي داخله:

DEEPSEEK_API_KEY=your_api_key_here

> ملاحظة: تأكد من استبدال your_api_key_here بمفتاح API الحقيقي الذي تحصل عليه من منصة DeepSeek.




---

5. تشغيل التطبيق

بعد الانتهاء من جميع الخطوات السابقة، يمكنك تشغيل تطبيقك بكتابة الأمر التالي:

python app.py

