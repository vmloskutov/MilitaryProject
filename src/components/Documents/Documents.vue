<template>
  <div>
    <div v-if="documents.length !== 0" class="my-document">
      <div v-if="count > 5" class="count">
        {{ count }} документов
      </div>
      <div v-else-if="count > 1">
        {{ count }} документа
      </div>
      <div v-else-if="count > 0">
        {{ count }} документ
      </div>

      <div v-for="year in documents" :key="year.year">
        <div class="cool-hr d-flex align-items-center">
          <hr class="mr-3">
          {{year.year}}
          <hr class="ml-3">
        </div>
        <el-row v-for="(item, index) in year.items" :key="item.id" class="document-card mt-3 mb-4">
          <el-col :span="2" style="font-size: 22px" class="mt-4">
            № {{ index+1 }}
          </el-col>
          <el-col :span="21">
            <div class="d-flex">
              <div>
                {{ item.publish_at | moment }}
              </div>
              <div class="ml-5" style="color: #76767A">
                {{ item.publish_places }}
              </div>
            </div>
            <div class="document-card-title">{{ item.title }}</div>
            <div v-for="(author, index) in item.authors" :key="index" class="document-card-authors">{{ author }}</div>
            <div class="document-card-annotation">{{ item.annotation }}</div>
          </el-col>
          <el-col :span="1" class="d-flex justify-content-end mt-4" >
            <el-popover
                    placement="bottom"
                    trigger="click"
            >
              <div style="text-align: center; margin: 0; padding: 0; font-size: 15px;">
                <div style="cursor:pointer;">Скачать</div>
                <div style="cursor:pointer;" @click="deleteArticle(item.id)">Удалить</div>
              </div>
              <div slot="reference" class="d-flex justify-content-center" style="width: 10px; cursor: pointer">
                <img src="../../assets/scienceWorks/popover.svg" alt="">
              </div>
            </el-popover>
          </el-col>
        </el-row>
      </div>

    </div>
    <div v-else class="my-document">
      Документы не найдены
    </div>
  </div>
</template>

<script>
import { getDocuments } from '@/api/documents'
import { deleteNir } from '@/api/delete'
import { deleteArticle } from '@/api/delete'
import { nir } from '@/api/nir'

import moment from 'moment'

export default {
  name: '',
  components: {},
  filters: {
    moment: function(date) {
      return moment(date).format('DD MMMM YYYY')
    }
  },
  data() {
    return {
      documents: [],
      count: undefined,
    }
  },
  watch: {
    '$route'(to, from) {
      const temp = this.$route.query.section
      this.fetchData(temp)
    }
  },
  created() {
    const temp = 'scienceArticles'
    this.fetchData(temp)
  },
  methods: {
    deleteArticle(id) {
      const deletedId = {
        'id': id
      }
      if (this.$route.query.section === 'scienceArticles') {
        deleteArticle(deletedId).then(response => {
          this.documents.forEach(item => {
            item.items = item.items.filter(i => {
              return i.id !== id
            })
          })
          this.documents = this.documents.filter(item => {
            return item.items.length !== 0
          })
          console.log('файл удален')
          this.count = this.count - 1
        }).catch(() => {
          console.log('Ошибка удаления файла')
        })
      } else {
        deleteNir(deletedId).then(response => {
          this.documents.forEach(item => {
            item.items = item.items.filter(i => {
              return i.id !== id
            })
          })
          this.documents = this.documents.filter(item => {
            console.log(item.items.length === 0)
            return item.items.length !== 0
          })
          console.log('файл удален')
          this.count = this.count - 1
        }).catch(() => {
          console.log('Ошибка удаления файла')
        })
      }
    },
    fetchData(target) {
      let author = this.$route.query.author ?  this.$route.query.author :  null
      let place = this.$route.query.place ?  this.$route.query.place :  null
      let start_date = this.$route.query.start_date ?  this.$route.query.start_date :  null
      let end_date = this.$route.query.end_date ?  this.$route.query.end_date :  null
      let text = this.$route.query.text ?  this.$route.query.text :  null
      let show = this.$route.query.show ?  this.$route.query.show :  'enabled'
      if (target === 'scienceArticles') {
        getDocuments(author, place, start_date, end_date, text, show).then(response => {
          this.documents = response.data.items
          this.count = response.data.total
        }).catch(() => {
          console.log('Данные по документам не указаны')
        })
      }
      if (target === 'scienceWorks') {
        nir(author, place, start_date, end_date, text).then(response => {
          this.documents = response.data.items
          this.count = response.data.total
        }).catch(() => {
          console.log('Данные по документам не указаны')
        })
      }


    },
    moment: function() {
      return moment()
    }
  },
}

</script>

<style scoped lang="scss">
  @import "style";
</style>
