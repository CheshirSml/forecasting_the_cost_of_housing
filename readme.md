# [ДИПЛОМНЫЙ ПРОЕКТ "Модель прогнозирования стоимости жилья для агенства недвижимости"](https://github.com/CheshirSml/forecasting_the_cost_of_housing/blob/main/forecasting_the_cost_of_housing.ipynb)

**Цель** - разработать модель, которая позволила бы агенству недвижимости обойти конкурентов по скорости и качеству сделок.  

**задачи:**

* очистить данные от выбросов и мусора;
* провести расведовательный анализ;
* построить несколько моделей и выбрать демонстрирующую лучший результат;
* разработать небольшой веб-сервис, принимающий данные об объекте, возвращающих прогноз стоимости.


**Метрика качества**
- Выполнены цели проекта
- Соблюдены и выполнены все этапы проекта, представлены обоснования и графики
- Решение размещено на Git hub
- Выполнен тестовый сабмит на вебсервер

<p><span id="TOC"></span></p>

## **ОГЛАВЛЕНИЕ**
<p> <a href="#1">1.ИНФОРМАЦИЯ О ДАННЫХ</a></p>
<p> <a href="#2">2.ЭТАПЫ РАБОТЫ НАД ПРОЕКТОМ</a></p>
<p> <a href="#3">3.РЕЗУЛЬТАТЫ</a></p>
<p> <a href="#4">4.КОДИРОВАНИЕ ПРИЗНАКОВ</a></p>
<p> <a href="#5">5.МОДЕЛИРОВАНИЕ</a></p>
<p> <a href="#6">6.ПРОДАКТ</a></p>



### <p><span id="#1">1.ИНФОРМАЦИЯ О ДАННЫХ</span></p>

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
* <span style=background-color:#D3D3D3>'status'</span> — статус продажи;  
* <span style=background-color:#D3D3D3>'private pool'</span> и <span style=background-color:#D3D3D3>'PrivatePool'</span> — наличие собственного бассейна;  
* <span style=background-color:#D3D3D3>'propertyType'</span> — тип объекта недвижимости;  
* <span style=background-color:#D3D3D3>'street'</span> — адрес объекта;  
* <span style=background-color:#D3D3D3>'baths'</span> — количество ванных комнат;  
* <span style=background-color:#D3D3D3>'homeFacts'</span> — сведения о строительстве объекта (содержит несколько типов сведений, влияющих на оценку объекта);  
* <span style=background-color:#D3D3D3>'fireplace'</span> — наличие камина;  
* <span style=background-color:#D3D3D3>'city'</span> — город;  
* <span style=background-color:#D3D3D3>'schools'</span> — сведения о школах в районе;  
* <span style=background-color:#D3D3D3>'sqft'</span> — площадь в футах;  
* <span style=background-color:#D3D3D3>'zipcode'</span> — почтовый индекс;  
* <span style=background-color:#D3D3D3>'beds'</span> — количество спален;  
* <span style=background-color:#D3D3D3>'state'</span> — штат;  
* <span style=background-color:#D3D3D3>'stories'</span> — количество этажей;  
* <span style=background-color:#D3D3D3>'mls-id'</span> и <span style=background-color:#D3D3D3>'MlsId'</span> — идентификатор MLS (Multiple Listing Service, система мультилистинга);  
* <span style=background-color:#D3D3D3>'target'</span> — цена объекта недвижимости (**целевой признак, который необходимо спрогнозировать**).

<p> <a href="#TOC">ОГЛАВЛЕНИЕ</a></p>

### <p><span id="#2">2.ЭТАПЫ РАБОТЫ НАД ПРОЕКТОМ</span></p>

1. Произведена отчистка данных от выбросов и пустых значений, преобразованы признаки.
2. Произведена оценка значимости признаков, сформированны новые признаки.
3. Произведен отбор значемых признаков.
4. Произведена нормализация числовых признаков.
5. Произведена кодировка категориальных признаков.
6. Построены несколько моделей с использованией подбора гиперпараметров. (Baseline(LR), Best features(LR), DecisionTreeRegressor, DecisionTreeRegressor(optimal), ElasticNetCV(optimal), RandomForestRegressor, RandomForestRegressor(best), GradientBoostingRegressor, CatBoostRegressor(Optimal))
7. Подготовлен сервер с сериализованной моделью и докер.

<p> <a href="#TOC">ОГЛАВЛЕНИЕ</a></p>

### <p><span id="#3">3.РЕЗУЛЬТАТЫ</span></p>

В результате выполнения проекта построенна модель CatBoostRegressor оптимально подходящая под решение поставленной задачи.


