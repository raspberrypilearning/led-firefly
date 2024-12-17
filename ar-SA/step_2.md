## قم بإعداد Raspberry Pi Pico الخاص بك

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
قم بتوصيل Raspberry Pi Pico وإعداد MicroPython.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> هي نسخة من لغة برمجة Python الخاصة بوحدات التحكم الدقيقة ، مثل Raspberry Pi Pico الخاص بك. يتيح لك MicroPython استخدام معرفتك ب Python لكتابة التعليمات البرمجية للتفاعل مع المكونات الإلكترونية.</p>

--- task ---

**اربط** الطرف الصغير من كابل USB الخاص بك إلى Raspberry Pi Pico.

![صورة لجهاز Raspberry Pi Pico متصل بالطرف الصغير لكابل USB.](images/pico-top-plug.png)

--- /task ---

--- task ---

**اربط** الطرف الآخر بجهاز الكمبيوتر أو الكمبيوتر المحمول أو Raspberry Pi.

![صورة لجهاز Raspberry Pi Pico متصل بحاسوب محمول بواسطة كابل USB.](images/plug-in-pico.png)

--- /task ---


--- task ---

افتح محرر Thonny.

--- /task ---

--- task ---

انظر إلى النص في الزاوية السفلية اليمنى من محرر Thonny. سيظهر لك إصدار Python المستخدم.

إذا لم يقل "MicroPython (Raspberry Pi Pico)" ، فانقر فوق النص وحدد "MicroPython (Raspberry Pi Pico)".

إذا لم يسبق لك استخدام MicroPython على Raspberry Pico ، فسيطالبك Thonny بإضافة البرنامج الثابت MicroPython. Click **Install MicroPython**.

--- /task ---

--- task ---

**التصحيح:**

--- collapse ---
---
title: حدث خطأ أثناء تثبيت البرنامج
---

إذا ظهرت لك رسالة خطأ أثناء التثبيت ، فقم بما يلي:
+ افصل Raspberry Pi Pico الخاص بك
+ أعد توصيل Raspberry Pi Pico الخاص بك
+ حاول تثبيت البرنامج الثابت مرة أخرى (قد تحتاج إلى الضغط على زر الإيقاف أولا)

![لقطة شاشة لرسالة خطأ توضح عدم إمكانية تثبيت البرنامج الثابت بشكل صحيح.](images/pico-firmware-error.PNG)

--- /collapse ---

--- collapse ---
---
title: لا أعرف ما إذا كان البرنامج مثبتا ولا يمكن الاتصال ب Pico الخاص بي
---

تأكد من توصيل Raspberry Pi Pico بالحاسوب باستخدام كبل micro USB. انقر على القائمة الموجودة في الزاوية السفلية اليمنى من نافذة Thonny الخاصة بك. ستظهر قائمة منبثقة تسرد مترجمي اللغة البرمجية المتاحين.

![قائمة منبثقة تعرض خيارا يقول إعداد المترجم الفوري.](images/no-pico-interpreter.png)

إذا لم تتمكن من رؤية Pico في القائمة (كما هو الحال في الصورة) ، فستحتاج إلى إعادة توصيل Raspberry Pi Pico أثناء الضغط على زر BOOTSEL لتثبيته كوحدة تخزين ، وإعادة تثبيت البرنامج باتباع الإرشادات الواردة في القسم أعلاه.

--- /collapse ---

--- collapse ---
---
title: تم تثبيت البرنامج ولكن ما زلت لا أستطيع الاتصال بجهاز Pico الخاص بي
---

ربما تستخدم نوعًا خاطئًا من كبل micro USB. قد يكون كبل micro USB الحالي تالفا أو مصمما فقط لنقل الطاقة إلى الأجهزة ولا يمكنه نقل البيانات. حاول تبديل الكابل إذا لم ينجح أي شيء آخر.

إذا كان جهاز Pico الخاص بك لا يزال غير متصل بعد تجربة كل هذه الأشياء ، فقد يكون **الجهاز نفسه** تالفًا وغير قادر على الاتصال.

--- /collapse ---

يمكنك العثور على مزيد من المعلومات في [دليل استخدام Raspberry Pi](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){: target = "_ blank"}.

--- /task ---

`picozero` هي مكتبة MicroPython للمبتدئين في Raspberry Pi Pico.

--- task ---

لإكمال المشاريع في هذا المسار ، ستحتاج إلى تثبيت مكتبة `picozero` كحزمة لمحرر Thonny.

في محرر Thonny، اختر **Tools** > **Manage packages**.

![تم تمييز قائمة أدوات محرر Thonny مع إدارة الحزم.](images/thonny-manage-packages.jpg)

--- /task ---

--- task ---

في النافذة المنبثقة 'Manage packages لـ Raspberry Pi Pico'، اكتب `picozero` وانقر فوق **Search on PyPi**.

![نتائج بحث إضافات Thonny تظهر picozero.](images/thonny-packages-picozero.jpg)

--- /task ---

--- task ---

انقر على **picozero** في نتائج البحث.

أنقر على **Install**.

![تم تمييز معلومات picozero مع زر "تثبيت".](images/thonny-install-package.jpg)

عند اكتمال التثبيت، أغلق نافذة الحزمة، ثم قم بإغلاق محرر Thonny وإعادة فتحه.

--- /task ---

إذا واجهت صعوبات في تثبيت مكتبة `picozero` في محرر Thonny ، فيمكنك تنزيل ملف المكتبة وحفظه في Raspberry Pi Pico.

[[[picozero-offline-install]]]
