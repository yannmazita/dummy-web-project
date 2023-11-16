<template>
    <h1>Accueil</h1>
    <div class="divider"></div>
    <article>
        <h1>Actualités</h1>
    </article>
    <div class="divider"></div>
    <section>
        <div class="flex justify-center">
            <div class="carousel w-full sm:w-1/2">
                <div id="slide1" class="carousel-item relative w-full">
                    <div class="flex items-center justify-center">
                        <h2>Agenda</h2>
                        <img :src="agendaImageUrl" class="w-full" />
                        <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                            <a href="#slide4" class="btn btn-circle">❮</a> 
                            <a href="#slide2" class="btn btn-circle">❯</a>
                        </div>
                    </div>
                </div> 
                <div id="slide2" class="carousel-item relative w-full">
                    <img :src="inscriptionImageUrl" class="w-full" />
                    <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                        <a href="#slide1" class="btn btn-circle">❮</a> 
                        <a href="#slide3" class="btn btn-circle">❯</a>
                    </div>
                </div> 
                <div id="slide3" class="carousel-item relative w-full">
                    <img :src="contactImageUrl" class="w-full" />
                    <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                        <a href="#slide2" class="btn btn-circle">❮</a> 
                        <a href="#slide4" class="btn btn-circle">❯</a>
                    </div>
                </div> 
                <div id="slide4" class="carousel-item relative w-full">
                    <img :src="boutiqueImageUrl" class="w-full" />
                    <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                        <a href="#slide3" class="btn btn-circle">❮</a> 
                        <a href="#slide1" class="btn btn-circle">❯</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <div class="divider"></div>
    <section>
        <h2>Les partenaires</h2>
    </section>
</template>

<script setup>
    import agendaImageUrl from '@/assets/images/home-page/agenda_image.jpg'
    import inscriptionImageUrl from '@/assets/images/home-page/inscription_image.jpg'
    import contactImageUrl from '@/assets/images/home-page/contact_image.jpg'
    import boutiqueImageUrl from '@/assets/images/home-page/boutique_image.jpeg'
</script>
