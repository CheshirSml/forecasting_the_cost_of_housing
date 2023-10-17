# [ДИПЛОМНЫЙ ПРОЕКТ "Модель прогнозирования стоимости жилья для агенства недвижимости"](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/forecasting_the_cost_of_housing.ipynb)

**Цель** - разработать модель, которая позволила бы агенству недвижимости обойти конкурентов по скорости и качеству сделок.  

**задачи:**

* очистить данные от выбросов и мусора;
* провести расведовательный анализ;
* построить несколько моделей и выбрать демонстрирующую лучший результат;
* разработать небольшой веб-сервис, принимающий данные об объекте, возвращающих прогноз стоимости.


<p><span id="TOC"></span></p>

## **ОГЛАВЛЕНИЕ**
<p> <a href="#1">1.Информация о проекте и данных</a></p>
<p> <a href="#2">2.Этапы работы над проектом</a></p>
<p> <a href="#3">3.Результаты</a></p>


### <p><span id="#1">1.Информация о проекте и данных</span></p>

#### Краткая информация о данных:

* Датасет содержит данные об объектах недвижимости США 
* [forecasting_the_cost_of_housing.ipynb](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/forecasting_the_cost_of_housing.ipynb) - Jupiter Notebook с проектом
* папка *web* содержит данные для продакта модели:
    * [server.py](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/app/server.py) - сервер на Flask 
    * [client.py](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/test/client.py) - клиент для тестирования
    * [best_cb_model.pkl](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/app/model/best_cb_model.pkl) - сериализованная модель
    * [Dockerfile](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/test/Dockerfile)
    * [uwsgi.ini](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/test/uwsgi.ini)
    * [requirements.txt](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/web/test/requirements.txt)

**Описание данных:**  
* *'status'* — статус продажи;  
* *'private pool'* и *'PrivatePool'* — наличие собственного бассейна;  
* *'propertyType'* — тип объекта недвижимости;  
* *'street'* — адрес объекта;  
* *'baths'* — количество ванных комнат;  
* *'homeFacts'* — сведения о строительстве объекта (содержит несколько типов сведений, влияющих на оценку объекта);  
* *'fireplace'* — наличие камина;  
* *'city'* — город;  
* *'schools'* — сведения о школах в районе;  
* *'sqft'* — площадь в футах;  
* *'zipcode'* — почтовый индекс;  
* *'beds'* — количество спален;  
* *'state'* — штат;  
* *'stories'* — количество этажей;  
* *'mls-id'* и *'MlsId'* — идентификатор MLS (Multiple Listing Service, система мультилистинга);  
* *'target'* — цена объекта недвижимости (**целевой признак, который необходимо спрогнозировать**).

<p> <a href="#TOC">ОГЛАВЛЕНИЕ</a></p>

### <p><span id="#2">2.Этапы работы над проектом</span></p>

1. Произведена отчистка данных от выбросов и пустых значений, преобразованы признаки.
2. Произведена оценка значимости признаков, сформированны новые признаки.
3. Произведен отбор значемых признаков.
4. Произведена нормализация числовых признаков.
5. Произведена кодировка категориальных признаков.
6. Построены несколько моделей с использованией подбора гиперпараметров. (Baseline(LR), Best features(LR), DecisionTreeRegressor, DecisionTreeRegressor(optimal), ElasticNetCV(optimal), RandomForestRegressor, RandomForestRegressor(best), GradientBoostingRegressor, CatBoostRegressor(Optimal))
7. Подготовлен сервер с сериализованной моделью и докер.

<p> <a href="#TOC">ОГЛАВЛЕНИЕ</a></p>

### <p><span id="#3">3.Результаты</span></p>

В результате выполнения проекта построенна модель CatBoostRegressor оптимально подходящая под решение поставленной задачи.

<p> <a href="#TOC">ОГЛАВЛЕНИЕ</a></p>
