<template>
  <div>
    <swiper v-bind:options="swiperOption">
      <swiper-slide>
        1
        <img src="@/assets/logo.png" />
      </swiper-slide>
      <swiper-slide>
        2
        <img src="@/assets/logo.png" />
      </swiper-slide>
      <swiper-slide>
        3
        <img src="@/assets/logo.png" />
      </swiper-slide>
      <swiper-slide>
        4
        <img src="@/assets/logo.png" />
      </swiper-slide>
      <swiper-slide>
        5
        <img src="@/assets/logo.png" />
      </swiper-slide>

      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/dist/css/swiper.css";

export default {
  name: "MySwiper",
  components: {
    swiper,
    swiperSlide,
  },
  data() {
    return {
      swiperOption: {
        loop: true,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
          disableOnInteraction: false,
        },

        // 设置显示的个数
        slidesPerView: 4,
        spaceBetween: 30,
        centeredSlides: true,

        // 3D效果
        effect: "coverflow",
        grabCursor: true,
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: true,
        },

        // 显示分页
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },

        // 设置点击箭头
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
    };
  },

  mounted() {},
};
</script>

<style scoped></style>
