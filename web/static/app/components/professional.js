new Vue({
  el: '#professional',
  data: {
    professional_uuid: PROFESSIONAL_UUID,
    week_days: WEEK,
    selected: {
      date: null,
      time: null,
    },
    currentYear: CURRENT_YEAR,
    currentWeek: CURRENT_WEEK,
  },
  computed: {

  },
  methods: {
    matchSelected: function (date, time) {
      return this.selected.date === date && this.selected.time === time;
    },
    select: function (available, date, time) {
      if (available) {
        this.selected.date = date;
        this.selected.time = time;
      }
    },
    handleNextWeek: function () {
      const self = this;
      const nextWeek = this.currentWeek + 1;
      client.get(`/professionals/${this.professional_uuid}/calendar/?week=${nextWeek}`)
      .then(function (response) {
        self.week_days = response.data;
        self.currentWeek = nextWeek;
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
    },
    handlePreviousWeek: function () {
      const self = this;
      const previousWeek = this.currentWeek - 1;
      client.get(`/professionals/${this.professional_uuid}/calendar/?week=${previousWeek}`)
      .then(function (response) {
        self.week_days = response.data;
        self.currentWeek = previousWeek;
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
    },
    handleCreateAppointment: function (e) {
      const self = this;
      const payload = {
        professional: this.professional_uuid,
        date: this.selected.date,
        time: this.selected.time,
      }
      client.post(`/appointments/`, payload)
      .then(function (response) {
        alert('CREADO!')
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
   }

  },
  mounted: function () {
    console.log('MOUNTED!')
  }
})
