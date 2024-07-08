import discord
from discord.ext import commands
from model import car_check 
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    if attachments:
        for attachment in attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            await ctx.send(f'успешно сохранено в images/{file_name}')
            class_name = car_check(attachment.filename)
            if class_name == 'tesla':
                await ctx.send(f'это марка машины: {class_name}.  Tesla Motors — автомобильная компания, основанная в 2003 году и ориентированная на производство премиальных спортивных электромобилей.
Штаб-квартира компании расположена в Кремниевой долине, штат Калифорния, США. Компания названа в честь всемирно известного учёного-электротехника Николы Тесла. Именно запатентованный Николой Тесла в 1888 году индукционный электродвигатель переменного тока положен в основу конструкции силовых агрегатов, устанавливаемых на автомобили Tesla.
В Россию автомобили Tesla официально не поставляются, однако начало развёртывания сети «Суперзарядок» планируется в 2016 году.')
            elif class_name == 'bmw':
                await ctx.send(f'это марка машины: {class_name}. это аббревиатура от Bayerische Motoren Werke GmbH, что переводится как «Баварские Моторные Заводы».\n В этом названии скрывается отсылка к родине компании — Баварии. Также оно указывает на изначальную линейку продукции BMW: двигатели для различных задач.')
            elif class_name == 'nissan':
                await ctx.send(f'это марка машины: {class_name}. Nissan Motor Co., Ltd. — японский автопроизводитель, входящий в Альянс Renault–Nissan–Mitsubishi. Основан в 1933 году в Иокогаме. По состоянию на 2022 год занимал 9-е место в мировом рейтинге, являясь вторым среди японских производителей после Toyota. Ведущий бренд в Китае, России и Мексике.')
            elif class_name == 'ferrari':
                await ctx.send(f'это марка машины: {class_name}. Ferrari — итальянская компания, выпускающая спорткары и гоночные автомобили. Основана в 1939 году. В 1947 году начала выпускать спортивные автомобили. С 1969 до 2016 год входила в концерн FIAT.\n На протяжении всей истории компания участвует в гонках, особенно в Формуле-1. Эмблема «Феррари» — гарцующий жеребец на жёлтом фоне. Традиционный цвет автомобилей — красный.')
            elif class_name == 'lamborghini':
                await ctx.send(f'это марка машины: {class_name}. Lamborghini ― итальянский производитель спортивных авто премиум-класса, которые считаются одними из самых дорогих, быстрых и надежных в мире. Индивидуальный выпуск моделей делает их обладателями эксклюзивных автомобилей с мощным 12-цилиндровым двигателем и непревзойденной скоростью.')
            elif class_name == 'rolls-royce':
                await ctx.send(f'это марка машины: {class_name}. Rolls-Royce — это британский производитель роскошных автомобилей с 1906 года. Они символизируют престиж и элегантность, собираются вручную и предлагают премиальные материалы. Модели включают Ghost, Phantom, Cullinan, Wraith, Dawn и Spectre, первый электромобиль компании.')
            elif class_name == 'volvo':
                await ctx.send(f'это марка машины: {class_name}. Volvo — компания мирового уровня с предприятиями в Швеции, Бельгии и Китае. Выпускает автомобили премиум-класса: седаны, универсалы, спортивные универсалы, внедорожники и автомобили повышенной проходимости. Основана в 1915 году как дочерняя компания SKF. В 1999 году Volvo продал своё легковое подразделение концерну Ford. В 2010 году владельцем Volvo стал китайский производитель Geely Automobile.')
            elif class_name == 'bently':
                await ctx.send(f'это марка машины: {class_name}. Bentley Motors Ltd. — британский производитель автомобилей класса «люкс», который с 1998 года является частью немецкого концерна Volkswagen AG.\n  В 2021 году у компании были модели: Bentley Flying Spur, Continental GT, Bentayga. В 2020 году представили стратегию развития на десять лет. Она направлена на снижение ущерба экологии путём выпуска более технологичных автомобилей. К 2026 году перейдут на выпуск гибридных и полностью электрических авто, а к 2030 году — только электрических.')
            elif class_name == 'toyota':
                await ctx.send(f'это марка машины: {class_name}. Toyota Motor Corporation — один из ведущих мировых автопроизводителей, предлагающий широкий ассортимент надёжных и качественных автомобилей под брендом Toyota. \n В России доступны различные модели Toyota, включая Corolla, Camry, C-HR, Fortuner, Highlander, Land Cruiser Prado, RAV4, Alphard, Hiace, Tacoma и другие. Для получения актуальной информации о доступных моделях, ценах и комплектациях рекомендуется посетить официальный сайт Toyota или обратиться к дилеру в вашем регионе.')
    else:
        await ctx.send("No attachments found./вы забыли загрузить картинку.")

bot.run("token")