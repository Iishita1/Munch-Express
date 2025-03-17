from app import app, db
from models import TajPalace, SarwaanaBhawan, PunjabGrill, DosaPlaza, BiryaniHouse, Baarista, MughalsKitchen

with app.app_context():
    # Dishes for TajPalace
    new_dish_tajpalace = [
        TajPalace(
            dish_name='Chole Bhature',
            dish_price=499,
            dish_image='https://t4.ftcdn.net/jpg/04/46/48/25/240_F_446482584_oKIkypOqslb4OfDBMi9zywW7Vc6tXNmv.jpg',
            dish_description='Authentic taste of Punjab with a modern touch.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        TajPalace(
            dish_name='Rajma Chawal',
            dish_price=669,
            dish_image='https://www.secondrecipe.com/wp-content/uploads/2017/08/rajma-chawal-1.jpg',
            dish_description='North India\'s most loved dish with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        TajPalace(
            dish_name='Amritsari Kulcha',
            dish_price=459,
            dish_image='https://media.istockphoto.com/id/1488738157/photo/channa-masala-with-amritsari-kulcha.jpg?s=612x612&w=0&k=20&c=CWdGzbqBBoXGimbX_oVkitkF2s4gBtPDWMXhWx4-1Ok=',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        TajPalace(
            dish_name='Palak Paneer',
            dish_price=159,
            dish_image='https://healthynibblesandbits.com/wp-content/uploads/2020/01/Saag-Paneer-FF.jpg',
            dish_description='Health+Taste with spicy flavor and touch of Olives.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        TajPalace(
            dish_name='Butter Chicken',
            dish_price=289,
            dish_image='https://masalaandchai.com/wp-content/uploads/2022/03/Butter-Chicken.jpg',
            dish_description='Made to perfection.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        TajPalace(
            dish_name='Fish Tikka',
            dish_price=699,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2022/05/shutterstock_1790057069.jpg',
            dish_description='Special tikka cooked till perfection.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        TajPalace(
            dish_name='Chicken Tikka',
            dish_price=399,
            dish_image='https://images.immediate.co.uk/production/volatile/sites/30/2022/08/Chicken-Tikka-99647a6.jpg?resize=900%2C471',
            dish_description='Hot chicken with elegant flavors.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        TajPalace(
            dish_name='Kerala Chicken Roast',
            dish_price=199,
            dish_image='https://www.yummytummyaarthi.com/wp-content/uploads/2016/03/1-33.jpg',
            dish_description='Chicken with South Indian flavors.',
            dish_category='Non-Veg',
            dish_rating=4.6
        ),
        TajPalace(
            dish_name='Makke di Roti, Sarson da Saag',
            dish_price=559,
            dish_image='https://sinfullyspicy.com/wp-content/uploads/2022/12/1.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        TajPalace(
            dish_name='Chettinad Chicken',
            dish_price=579,
            dish_image='https://butfirstchai.com/wp-content/uploads/2023/01/chicken-chettinad-curry-recipes.jpg',
            dish_description='South Indian pepper chicken.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        TajPalace(
            dish_name='Aaloo Parantha',
            dish_price=669,
            dish_image='https://media.istockphoto.com/id/1418692758/photo/north-indian-famous-food-aloo-paratha-with-mango-pickle-and-butter.jpg?s=612x612&w=0&k=20&c=JDbBS-5EcSOKUeossLW2NufdKE0Mg7zFZV5ZBLdbpUE=',
            dish_description='Authentic Punjabi taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        TajPalace(
            dish_name='Masala Dosa',
            dish_price=499,
            dish_image='https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?cs=srgb&dl=pexels-saveurssecretes-5560763.jpg&fm=jpg',
            dish_description='South Indian special.',
            dish_category='Veg',
            dish_rating=4.6
        )
    ]

    # Dishes for SarwaanaBhawan
    new_dish_sarwaana = [
        SarwaanaBhawan(
            dish_name='Paneer Kofta',
            dish_price=499,
            dish_image='https://static.toiimg.com/thumb/60935758.cms?imgsize=669888&width=800&height=800',
            dish_description='Authentic taste of Punjab with a modern touch.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        SarwaanaBhawan(
            dish_name='Rajma Chawal',
            dish_price=669,
            dish_image='https://www.secondrecipe.com/wp-content/uploads/2017/08/rajma-chawal-1.jpg',
            dish_description='North India\'s most loved dish with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        SarwaanaBhawan(
            dish_name='Chole Chawal',
            dish_price=459,
            dish_image='https://sattvakitchen.com/wp-content/uploads/2024/05/CHOLE-CHAWAL-iStock-1917310235.jpg',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        SarwaanaBhawan(
            dish_name='Palak Paneer',
            dish_price=159,
            dish_image='https://healthynibblesandbits.com/wp-content/uploads/2020/01/Saag-Paneer-FF.jpg',
            dish_description='Health+Taste with an authentic style. Served hot.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        SarwaanaBhawan(
            dish_name='Paneer Tikka',
            dish_price=289,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6bSpmG6GbOwP8-y5DxeaUm5AxWQG8-rOiYw&s',
            dish_description='Made to perfection.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        SarwaanaBhawan(
            dish_name='Chili Paneer',
            dish_price=699,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlxATEp1CGqHea1gWMln5jPIDjlw4yS09t2g&s',
            dish_description='Special paneer cooked till perfection.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        SarwaanaBhawan(
            dish_name='Mushroom Tikka',
            dish_price=399,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGbwS_2N8BYNqDlEwA6C3TA0GKXV7QCBGBNg&s',
            dish_description='Hot mushroom with elegant flavors.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        SarwaanaBhawan(
            dish_name='Soya Chaamp Roast',
            dish_price=199,
            dish_image='https://www.yummytummyaarthi.com/wp-content/uploads/2016/03/1-33.jpg',
            dish_description='Soya Chaap with South Indian flavors.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        SarwaanaBhawan(
            dish_name='Malai Kofta',
            dish_price=559,
            dish_image='https://img.freepik.com/premium-photo/malai-kofta-curry-is-mughlai-special-recipe-served-bowl-selective-focus_466689-33336.jpg',
            dish_description='Indian Taste.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        SarwaanaBhawan(
            dish_name='Kadai Paneer',
            dish_price=579,
            dish_image='https://www.cubesnjuliennes.com/wp-content/uploads/2020/03/Best-Kadai-Paneer-Recipe.jpg',
            dish_description='Indian pepper paneer.',
            dish_category='Veg',
            dish_rating=4.0
        ),
        SarwaanaBhawan(
            dish_name='Aaloo Parantha',
            dish_price=669,
            dish_image='https://media.istockphoto.com/id/1418692758/photo/north-indian-famous-food-aloo-paratha-with-mango-pickle-and-butter.jpg?s=612x612&w=0&k=20&c=JDbBS-5EcSOKUeossLW2NufdKE0Mg7zFZV5ZBLdbpUE=',
            dish_description='Authentic Punjabi taste.',
            dish_category='Veg',
            dish_rating=4.9
        ),
        SarwaanaBhawan(
            dish_name='Masala Dosa',
            dish_price=499,
            dish_image='https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?cs=srgb&dl=pexels-saveurssecretes-5560763.jpg&fm=jpg',
            dish_description='South Indian special.',
            dish_category='Veg',
            dish_rating=4.0
        )
    ]

    # Dishes for PunjabGrill
    new_dish_punjabgrill = [
        PunjabGrill(
            dish_name='Dal Makhani',
            dish_price=499,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAM_sU4h_Iz_foXrcRwo2H0NBHIgFdCv_KbA&s',
            dish_description='Authentic taste of Punjab with a modern touch.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        PunjabGrill(
            dish_name='Lacha Parantha',
            dish_price=669,
            dish_image='https://static.toiimg.com/thumb/85887113.cms?imgsize=119034&width=800&height=800',
            dish_description='North India\'s most loved dish with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        PunjabGrill(
            dish_name='Mughlai Kulcha',
            dish_price=459,
            dish_image='https://static01.nyt.com/images/2020/10/08/dining/fh-mughlai-paratha/merlin_177593343_8829b4e7-f3c2-478e-927d-e5ab263ae515-superJumbo.jpg',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        PunjabGrill(
            dish_name='Palak Paneer',
            dish_price=159,
            dish_image='https://healthynibblesandbits.com/wp-content/uploads/2020/01/Saag-Paneer-FF.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        PunjabGrill(
            dish_name='Handi Biryani',
            dish_price=289,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2022/06/mutton-hyderabadi-biryani-01.jpg',
            dish_description='Biryani with North Indian touch.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Non Veg Thali',
            dish_price=1299,
            dish_image='https://i.pinimg.com/736x/20/92/48/2092483fde63dc2c9e3f2a0038c8af1f.jpg',
            dish_description='Special non-veg thali.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Chicken Roulade',
            dish_price=399,
            dish_image='https://thecozycook.com/wp-content/uploads/2024/01/Chicken-Roulade-1-1.jpg',
            dish_description='Hot chicken with elegant flavors.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Chicken Lollipops',
            dish_price=199,
            dish_image='https://media.istockphoto.com/id/1091602054/photo/szechuan-chicken-which-is-a-popular-indo-chinese-non-vegetarian-recipe-served-in-a-plate-with.jpg?s=612x612&w=0&k=20&c=n1mIhGKsTFgDno11fS_XzioDFT548ZIF13Q-QDK6bAg=',
            dish_description='Chicken with South Indian flavors.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Makke di Roti, Sarson da Saag',
            dish_price=559,
            dish_image='https://sinfullyspicy.com/wp-content/uploads/2022/12/1.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Chicken Korma',
            dish_price=579,
            dish_image='https://static.vecteezy.com/system/resources/previews/038/972/486/non_2x/ai-generated-chicken-korma-isolated-on-white-indian-cuisine-meat-curry-dish-with-coconut-milk-masala-asian-food-photo.jpg',
            dish_description='Indian pepper chicken.',
            dish_category='Non-Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Aaloo Parantha',
            dish_price=669,
            dish_image='https://media.istockphoto.com/id/1418692758/photo/north-indian-famous-food-aloo-paratha-with-mango-pickle-and-butter.jpg?s=612x612&w=0&k=20&c=JDbBS-5EcSOKUeossLW2NufdKE0Mg7zFZV5ZBLdbpUE=',
            dish_description='Authentic Punjabi taste.',
            dish_category='Veg',
            dish_rating=4.9
        ),
        PunjabGrill(
            dish_name='Chicken Shawarma',
            dish_price=499,
            dish_image='https://cookingorgeous.com/wp-content/uploads/2024/01/easy-homemade-lebanese-chicken-shawarma-20.jpg',
            dish_description='Indian Special.',
            dish_category='Non-Veg',
            dish_rating=4.9
        )
    ]

    # Dishes for DosaPlaza
    new_dish_dosaplaza = [
        DosaPlaza(
            dish_name='Plain Idli',
            dish_price=499,
            dish_image='https://t3.ftcdn.net/jpg/01/61/13/66/360_F_161136674_NgVFcPtWfwLPY03NpJUrSiH9oDvma9Rn.jpg',
            dish_description='Authentic taste of South with a modern touch.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        DosaPlaza(
            dish_name='Masala Idli',
            dish_price=669,
            dish_image='https://cookilicious.com/wp-content/uploads/2016/06/Mini-Masala-Idli-5.jpg',
            dish_description='South India\'s most loved dish with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        DosaPlaza(
            dish_name='Vada Sambhar',
            dish_price=459,
            dish_image='https://t3.ftcdn.net/jpg/11/19/61/12/360_F_1119611210_HILd0dQ1VtzSn3L8z5wHjxII9Nlh7NJl.jpg',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        DosaPlaza(
            dish_name='Plain Dosa',
            dish_price=159,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK63B0GlU6SASc3EXBh3Ip3pKRKqASVEzrIg&s',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        DosaPlaza(
            dish_name='Handi Biryani',
            dish_price=289,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2022/06/mutton-hyderabadi-biryani-01.jpg',
            dish_description='Hyderabadi Biryani.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Non Veg Thali',
            dish_price=1299,
            dish_image='https://i.pinimg.com/736x/20/92/48/2092483fde63dc2c9e3f2a0038c8af1f.jpg',
            dish_description='Special non-veg thali.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Chicken Roulade',
            dish_price=399,
            dish_image='https://thecozycook.com/wp-content/uploads/2024/01/Chicken-Roulade-1-1.jpg',
            dish_description='Hot chicken with elegant flavors.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Chicken Channet',
            dish_price=199,
            dish_image='https://drop.ndtv.com/albums/COOKS/5-non-veg-south_637945968901459445/637945968919611327.jpeg',
            dish_description='Chicken with South Indian flavors.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Veg Sambhar',
            dish_price=559,
            dish_image='https://t3.ftcdn.net/jpg/04/19/77/14/360_F_419771473_T13jOSeb0aBECVw1ekoQO3d0R4hxFHMY.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Chicken Korma',
            dish_price=579,
            dish_image='https://static.vecteezy.com/system/resources/previews/038/972/486/non_2x/ai-generated-chicken-korma-isolated-on-white-indian-cuisine-meat-curry-dish-with-coconut-milk-masala-asian-food-photo.jpg',
            dish_description='Indian pepper chicken.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Urad Dal Rice Uttapam',
            dish_price=669,
            dish_image='https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/32599/images/1d6186b-d38e-ae6b-117-10771d4ecdb_img_67_urad-dal-rice-uttapam-or-dosa_1534142211.jpg',
            dish_description='Authentic South Indian taste.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        DosaPlaza(
            dish_name='Chetinad Fish',
            dish_price=499,
            dish_image='https://drop.ndtv.com/albums/COOKS/5-non-veg-south_637945968901459445/637945968925794905.jpeg',
            dish_description='South Indian special.',
            dish_category='Non-Veg',
            dish_rating=4.8
        )
    ]

    # Dishes for BiryaniHouse
    new_dish_biryanihouse = [
        BiryaniHouse(
            dish_name='Veg Hyderabadi Biryani',
            dish_price=499,
            dish_image='https://kannanskitchen.com/wp-content/uploads/2021/04/DSC_1079_1.jpg',
            dish_description='Authentic taste of Hyderabad with a modern touch.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        BiryaniHouse(
            dish_name='Veg Pulao',
            dish_price=669,
            dish_image='https://t4.ftcdn.net/jpg/04/18/22/71/360_F_418227121_mGoGy7ZE2jAkq07OnN599QU7PVuhVT57.jpg',
            dish_description='South India\'s most loved dish with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.9
        ),
        BiryaniHouse(
            dish_name='Vada Sambhar',
            dish_price=459,
            dish_image='https://t3.ftcdn.net/jpg/11/19/61/12/360_F_1119611210_HILd0dQ1VtzSn3L8z5wHjxII9Nlh7NJl.jpg',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Plain Dosa',
            dish_price=159,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK63B0GlU6SASc3EXBh3Ip3pKRKqASVEzrIg&s',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.6
        ),
        BiryaniHouse(
            dish_name='Handi Biryani',
            dish_price=289,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2022/06/mutton-hyderabadi-biryani-01.jpg',
            dish_description='Handi Biryani.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Non Veg Thali',
            dish_price=1299,
            dish_image='https://i.pinimg.com/736x/20/92/48/2092483fde63dc2c9e3f2a0038c8af1f.jpg',
            dish_description='Special non-veg thali.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Beary Biryani',
            dish_price=399,
            dish_image='https://kitchenmai.com/wp-content/uploads/2020/08/chicken_beary_new_blog.jpg',
            dish_description='Chicken biryani with elegant flavors.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Chicken Channet',
            dish_price=199,
            dish_image='https://drop.ndtv.com/albums/COOKS/5-non-veg-south_637945968901459445/637945968919611327.jpeg',
            dish_description='Chicken with South Indian flavors.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Veg Sambhar',
            dish_price=559,
            dish_image='https://t3.ftcdn.net/jpg/04/19/77/14/360_F_419771473_T13jOSeb0aBECVw1ekoQO3d0R4hxFHMY.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Bombay Biryani',
            dish_price=579,
            dish_image='https://t4.ftcdn.net/jpg/09/28/82/47/360_F_928824793_tdXEOOB4ItBHAQZuxIVtc4CzsDCJgr07.jpg',
            dish_description='Bombay style Biryani.',
            dish_category='Non-Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Urad Dal Rice Uttapam',
            dish_price=669,
            dish_image='https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/32599/images/1d6186b-d38e-ae6b-117-10771d4ecdb_img_67_urad-dal-rice-uttapam-or-dosa_1534142211.jpg',
            dish_description='Authentic South Indian taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        BiryaniHouse(
            dish_name='Hyderabadi Biryani',
            dish_price=499,
            dish_image='https://purendesi.in/wp-content/uploads/2024/12/Andhra-Style-Chicken-Biryani.jpg',
            dish_description='Hyderabad special.',
            dish_category='Non-Veg',
            dish_rating=4.9
        )
    ]

    # Dishes for Baarista
    new_dish_baarista = [
        Baarista(
            dish_name='Honey Lavender Latte',
            dish_price=449,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfsAKb5NX1LNdFHnspKv4o45avYZDzTYBsrQ&s',
            dish_description='House-made lavender syrup, local honey, espresso, steamed milk.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Caramel Brulee Latte',
            dish_price=449,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNNdZ5Q4cx72sr79f9ZOw-vnkQ9FIEq0-ssg&s',
            dish_description='Torched caramel, espresso, steamed milk, whipped cream.',
            dish_category='Beverage',
            dish_rating=4.6
        ),
        Baarista(
            dish_name='Maple Cinnamon Latte',
            dish_price=449,
            dish_image='https://chelseapeachtree.com/wp-content/uploads/2020/10/Maple-Cinnamon-Vanilla-Cinnamon-Latte-1.jpg',
            dish_description='Pure maple syrup, cinnamon, espresso, steamed milk.',
            dish_category='Beverage',
            dish_rating=4.7
        ),
        Baarista(
            dish_name='Rose Cardamom Latte',
            dish_price=449,
            dish_image='https://www.facebook.com/photo.php?fbid=2404756346423050&id=1855958777969479&set=a.1863227880575902',
            dish_description='Rose water, cardamom syrup, espresso, steamed milk, dried rose petals.',
            dish_category='Beverage',
            dish_rating=4.8
        ),
        Baarista(
            dish_name='Cappuccino',
            dish_price=349,
            dish_image='https://www.livingnorth.com/article/an-expert-guide-to-making-the-perfect-cappuccino-at-home',
            dish_description='Rich espresso topped with velvety steamed milk and creamy foam.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Latte',
            dish_price=299,
            dish_image='https://staresso.com/blogs/espresso/what-is-a-latte',
            dish_description='Smooth espresso with steamed milk and a light layer of foam.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Americano',
            dish_price=249,
            dish_image='https://crave-worthy.com/americano-coffee-recipe/',
            dish_description='Espresso shots topped with hot water for a rich cup of coffee.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Pour Over',
            dish_price=349,
            dish_image='https://www.javapresse.com/blogs/pour-over/mastering-water-pouring-technique-pour-over-coffee',
            dish_description='Hand-crafted coffee made to order with single-origin beans.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Iced Latte',
            dish_price=349,
            dish_image='https://www.bbcgoodfood.com/recipes/iced-latte',
            dish_description='Chilled espresso with cold milk and ice.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Cold Brew',
            dish_price=349,
            dish_image='https://ineffablecoffee.com/en/cold-brew-coffee/',
            dish_description='Smooth, slow-steeped coffee served over ice.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Nitro Cold Brew',
            dish_price=399,
            dish_image='https://www.coffeeisland.gr/blog/en/nitro-cold-brew/',
            dish_description='Cold brew infused with nitrogen for a creamy, stout-like texture.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Iced Matcha Latte',
            dish_price=449,
            dish_image='https://www.foodandwine.com/recipes/iced-matcha-latte',
            dish_description='Premium grade matcha green tea with cold milk over ice.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='London Fog',
            dish_price=349,
            dish_image='https://www.wifemamafoodie.com/almond-milk-london-fog-with-lavender/',
            dish_description='Earl Grey tea with vanilla syrup and steamed milk.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Golden Turmeric Latte',
            dish_price=399,
            dish_image='https://nest-wellness.com/recipes/drinks/turmeric-golden-milk-spice-mix/',
            dish_description='Turmeric, ginger, honey, and steamed milk with a pinch of black pepper.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Chai Latte',
            dish_price=349,
            dish_image='https://liliebakery.fr/en/Chai-Latte/',
            dish_description='Spiced black tea concentrate with steamed milk.',
            dish_category='Beverage',
            dish_rating=4.5
        ),
        Baarista(
            dish_name='Hot Chocolate',
            dish_price=299,
            dish_image='https://cafedesireonline.in/products/hot-chocolate-1kg',
            dish_description='Rich, creamy hot chocolate topped with whipped cream.',
            dish_category='Beverage',
            dish_rating=4.5
        )
    ]

    # Dishes for MughalsKitchen
    new_dish_mughalskitchen = [
        MughalsKitchen(
            dish_name='Shami Kebab',
            dish_price=499,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSym-jXobbiKbwJjduxcTn93Ab90lLmTNreTg&s',
            dish_description='Authentic taste of Mughals with a modern touch.',
            dish_category='Veg',
            dish_rating=4.9
        ),
        MughalsKitchen(
            dish_name='Dahi Kebab',
            dish_price=669,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnV3AhioHQnqye0hgkuYSCuerovwrpsZQOQw&s',
            dish_description='India\'s most loved kebab with an aesthetic look.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Tofu Kebab',
            dish_price=459,
            dish_image='https://itsallgoodvegan.com/wp-content/uploads/2021/01/Primal-Kitchen-08.jpg',
            dish_description='Old taste. Modern look with the same authentic taste.',
            dish_category='Veg',
            dish_rating=4.7
        ),
        MughalsKitchen(
            dish_name='Veg Seekh Kebab',
            dish_price=159,
            dish_image='https://bakefresh.net/wp-content/uploads/2024/03/IMG_8834-scaled-735x1102.jpg',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.5
        ),
        MughalsKitchen(
            dish_name='Chicken Kebab',
            dish_price=289,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2020/12/Chicken-Kebab.jpg',
            dish_description='Made to perfection.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Fish Kebab',
            dish_price=699,
            dish_image='https://www.licious.in/blog/wp-content/uploads/2022/06/fish-kebabs-final.jpg',
            dish_description='Special tikka cooked till perfection.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Mutton Kebab',
            dish_price=399,
            dish_image='https://foodiesterminal.com/wp-content/uploads/2019/04/Mutton-seekh-kabab-recipe-22.jpg',
            dish_description='Hot mutton kebab with elegant flavors.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Cheesy Chicken Kebab',
            dish_price=699,
            dish_image='https://www.oliviascuisine.com/wp-content/uploads/2019/07/grilled-cheese-skewers-IG-720x720.jpg',
            dish_description='Chicken with South Indian flavors.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Soya Kebab',
            dish_price=559,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPLldqET8-Ay2FacC6z3iM_PfKK1YA2QLx5g&s',
            dish_description='Health+Taste.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Chettinad Chicken Kebab',
            dish_price=579,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRt-4HbF-XvZ9Wis8dTgxNQ2677kqgX5HLaXA&s',
            dish_description='South Indian pepper chicken.',
            dish_category='Non-Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Paneer Tikka Kebab',
            dish_price=669,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ2WY2YmIJtXrpmDToEHwJIOAcyBefjpFwXg&s',
            dish_description='Authentic Punjabi taste.',
            dish_category='Veg',
            dish_rating=4.8
        ),
        MughalsKitchen(
            dish_name='Achari Kebab',
            dish_price=499,
            dish_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl1Zd6PSAkbMUichi4VvGcCxTlHTo1kiedCQ&s',
            dish_description='South Indian special.',
            dish_category='Veg',
            dish_rating=4.8
        )
    ]

    # Save all objects to the database
    db.session.bulk_save_objects(new_dish_tajpalace)
    db.session.bulk_save_objects(new_dish_sarwaana)
    db.session.bulk_save_objects(new_dish_punjabgrill)
    db.session.bulk_save_objects(new_dish_dosaplaza)
    db.session.bulk_save_objects(new_dish_biryanihouse)
    db.session.bulk_save_objects(new_dish_baarista)
    db.session.bulk_save_objects(new_dish_mughalskitchen)
    db.session.commit()

    # Verify the data
    dishes = MughalsKitchen.query.all()
    for dish in dishes:
        print(dish.dish_name, dish.dish_price, dish.dish_description)