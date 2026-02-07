# OOP-AI
For AI (Python advanced OOP (2))

## Evaluation (100-point, OOP-only)
Score: 92 / 100  
Level: Middle

This score is based only on OOP structure and requirements (ABC, inheritance, composition, DI, SOLID, classmethod/staticmethod, property). Model logic correctness is not counted per your request.

## Rubric and Detailed Assessment (OOP-only)

1) Project setup (5 pts)
- Expected: folder structure and files exist
- Result: ✅ 5/5

2) ABC + Interface (10 pts)
- Expected: `MLModel` is abstract with `fit`/`predict`, abstract instantiation error noted
- Result: ✅ 10/10

3) Inheritance: `SklearnModel` (15 pts)
- Expected: `fit(self, X, y)` sets `is_fitted`, `predict(self, X)` raises error if not fitted
- Result: ✅ 15/15

4) Inheritance: `TorchModel` (10 pts)
- Expected: `fit(self, X, y)` and `predict(self, X)` match base signature
- Result: ✅ 10/10

5) Composition: `ModelService` (10 pts)
- Expected: `train` and `infer` use injected model; composition explanation
- Result: ✅ 10/10

6) Dependency Injection in `main.py` (10 pts)
- Expected: inject model instances and preprocessor; train then infer for both
- Result: ✅ 10/10

7) `@property` `name` (5 pts)
- Expected: each child class returns fixed names (`sklearn_dummy`, `torch_dummy`)
- Result: ⚠️ 3/5  
  - Base property returns class-based name; children do not override

8) `@classmethod` / `@staticmethod` (10 pts)
- Expected: `from_config` returns `cls(...)`, `normalize` does min-max safely
- Result: ⚠️ 6/10  
  - `from_config` returns a dict, not an instance  
  - `normalize` is correct

9) SOLID (Open/Closed + SRP) (15 pts)
- Expected: `RuleBasedModel` works without service changes; preprocessor injected
- Result: ✅ 15/15

10) Mini tests (10 pts)
- Expected: errors before training, normalize edge-case, rule model works
- Result: ⚠️ 8/10  
  - `infer` before `train` is commented out

## Why Level = Middle
- ABC, inheritance, composition, DI, and SOLID are all used correctly
- Two OOP spec mismatches remain (`name`, `from_config`)
- One mini-test is present but commented

## What to Fix to Reach Senior (OOP-only)
- Override `name` in child classes to return fixed values
- Make `from_config` return `cls(...)`
- Uncomment and run the `infer`-before-`train` check

## Suggested Quick Checks
- Call `infer` before `train` and confirm proper error
- Run `TorchModel.normalize([10, 10, 10])`
- Add and test `RuleBasedModel` with `ModelService`

## Baholash (100 ballik, faqat OOP)
Ball: 92 / 100  
Daraja: Middle

Bu baho faqat OOP talablari va struktura bo‘yicha berildi (ABC, inheritance, composition, DI, SOLID, classmethod/staticmethod, property). Model logikasi xatolari hisobga olinmadi.

## Mezon va Batafsil Tahlil (faqat OOP)

1) Loyiha tayyorligi (5 ball)
- Kutilgan: papka va fayllar to‘g‘ri yaratilgan
- Natija: ✅ 5/5

2) ABC + Interface (10 ball)
- Kutilgan: `MLModel` abstract, `fit`/`predict` abstractmethod, instans yaratishda xato izohi yozilgan
- Natija: ✅ 10/10

3) Inheritance: `SklearnModel` (15 ball)
- Kutilgan: `fit(self, X, y)` `is_fitted` ni o‘rnatadi, `predict(self, X)` train bo‘lmasa error tashlaydi
- Natija: ✅ 15/15

4) Inheritance: `TorchModel` (10 ball)
- Kutilgan: `fit(self, X, y)` va `predict(self, X)` bazaviy signature’ga mos bo‘lishi kerak
- Natija: ✅ 10/10

5) Composition: `ModelService` (10 ball)
- Kutilgan: `train` va `infer` inject qilingan modelni ishlatadi; composition izohi bor
- Natija: ✅ 10/10

6) Dependency Injection `main.py` da (10 ball)
- Kutilgan: model va preprocessor tashqaridan beriladi; avval train, keyin infer
- Natija: ✅ 10/10

7) `@property` `name` (5 ball)
- Kutilgan: child class lar `sklearn_dummy`, `torch_dummy` qaytaradi
- Natija: ⚠️ 3/5  
  - `name` faqat base class’da umumiy yozilgan, child class’da override qilinmagan

8) `@classmethod` / `@staticmethod` (10 ball)
- Kutilgan: `from_config` `cls(...)` qaytaradi, `normalize` min-max ishlaydi
- Natija: ⚠️ 6/10  
  - `from_config` instance emas, dict qaytargan  
  - `normalize` to‘g‘ri ishlaydi

9) SOLID (Open/Closed + SRP) (15 ball)
- Kutilgan: `RuleBasedModel` servisga tegmasdan ishlaydi; preprocessor injection qilingan
- Natija: ✅ 15/15

10) Mini testlar (10 ball)
- Kutilgan: train oldin infer error, normalize edge-case, rule model ishlashi
- Natija: ⚠️ 8/10  
  - `infer` `train`dan oldin chaqirish komment qilingan

## Nega daraja = Middle
- ABC, inheritance, composition, DI va SOLID to‘g‘ri ishlatilgan
- `name` va `from_config` bo‘yicha kichik OOP mos kelmasliklar bor
- Mini testlardan biri komment qilingan

## Senior bo‘lish uchun nimalarni tuzatish kerak (faqat OOP)
- `name` property’ni har bir child class’da override qilish
- `from_config` `cls(...)` qaytarsin
- `infer` `train`dan oldin chaqirishni kommentdan chiqarish

## Tezkor tekshiruvlar
- `infer`ni `train`dan oldin chaqirib error tekshirish
- `TorchModel.normalize([10, 10, 10])` ni tekshirish
- `RuleBasedModel`ni `ModelService` bilan sinash
