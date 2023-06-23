## سوف تصنع

في هذا المشروع ، ستستخدم Raspberry Pi Pico لصنع يراعة LED تومض بنمط معين ، تمامًا مثل اليراعات في الطبيعة ، وتوصيل مفتاح للتحكم في الضوء.

[[[flashing-light-warning]]]

<div style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;display: flex; flex-wrap: wrap'>
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
المتحكم الدقيق <span style="color: #0faeb0">microcontroller</span> هو جهاز حوسبة صغير يمكنه تشغيل التعليمات البرمجية والتفاعل مع <span style="color: #0faeb0">المكونات الإلكترونية</span> (مثل الأزرار والأضواء). عادة ما يتم تصميمه لإكمال مهمة واحدة ، ولا يحتوي على <span style="color: #0faeb0">نظام تشغيل</span>. 
Raspberry Pi Pico هو متحكم دقيق منخفض التكلفة يمكن استخدامه من قبل المبتدئين ويمكن استخدامه أيضا من قبل الخبراء لتطوير المنتجات الإلكترونية.
</div>
<div>
![رسم يد تحمل Raspberry Pi Pico.](images/pico-hand.jpg){:width="300px"}
</div>
</div>

<br/>
سوف تقوم بمايلي:

+ تعرف على "المتحكم الدقيق" Raspberry Pi Pico **microcontroller**
+ قم بتوصيل LED ومفتاح مصنوع من أسلاك التوصيل إلى المنافذ الموجودة في **Raspberry Pi Pico**
+ قم ببرمجة Raspberry Pi Pico باستخدام **MicroPython** و Thonny

--- no-print ---

--- task ---

يوضح هذا المثال وميض LED لتقليد يراعة حقيقية! هل يمكنك تحديد النمط المتكرر في الومضات؟

![رسم متحرك ل LED يراعة يومض "يشتعل وينطفئ"](images/firefly-blink.gif){:width="300px"}

--- /task ---

--- /no-print ---

--- print-only ---

--- task ---

يوضح هذا المثال يراعة LED. سوف يومض LED الخاص بك لتقليد اليراعة الحقيقية!

![مصباح LED مع شريط لاصق ملتصق به لتشكيل أجنحة. يوجد سلكان موصلان متصلان بمصباح LED ، أحدهما مزود بمقاومة مثبتة في مكانها بواسطة شريط كهربائي.](images/showcase_static.png)

--- /task ---

--- /print-only ---

لإتمام هذا المشروع ، ستحتاج إلى:

**الأجهزة**

يمكنك شراء كافة الأجهزة المطلوبة لهذا المشروع والمشاريع الأخرى في هذا المسار من متجر [Pimoroni web store.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

+ Raspberry Pi Pico مع رؤوس توصيل ملحومة عليه
+ كابل **data** USB A الى micro USB
+ 1× LED أصفر (أو أي لون تفضله)
+ 1× 100Ω مقاومة (أي مقاومة من 75Ω إلى 220Ω سوف تعمل)
+ 1 × سلك توصيل دبوس - مقبس
+ 3 × سلك توصيل مقبس - مقبس
+ اختياري: شريط لاصق، الشريط غير المرئي يعمل بشكل أفضل

[[[pin-socket-jumper-wires]]]

**البرمجيات**

+ Thonny - يمكن إكمال هذا المشروع باستخدام محرر Thonny Python، والذي يمكن تثبيته على أنظمة Linux, Windows أو Mac

[[[thonny-install]]]

[[[change-theme-thonny]]]

![](http://code.org/api/hour/begin_rp_ledfirefly.png)
