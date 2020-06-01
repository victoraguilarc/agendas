new Vue({
  el: '#doctor',
  data: {
    doctor_uuid: DOCTOR_UUID,
    week_days: WEEK,
    selected: {
      date: null,
      time: null,
    },
    currentYear: CURRENT_YEAR,
    currentWeek: CURRENT_WEEK,
    successModal: null,
    successAppointment: null,
  },
  computed: {

  },
  methods: {
    handleGoProfile: function(){
      window.location.href = "/profile/";
    },
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
      client.get(`/doctors/${this.doctor_uuid}/calendar/?week=${nextWeek}`)
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
      client.get(`/doctors/${this.doctor_uuid}/calendar/?week=${previousWeek}`)
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
      // console.log(this.$refs.successModal);
      const self = this;
      const payload = {
        doctor_uuid: this.doctor_uuid,
        date: this.selected.date,
        time: this.selected.time,
      }
      client.post('/appointments/', payload)
      .then(function (response) {
        self.week_days = response.data.week_days;
        self.successAppointment = response.data.appointment;
        console.log(self.successAppointment);
        Vue.nextTick(function () {
          self.successModal.modal('show');
          self.selected = { date: null, time: null };
        })
      })
      .catch(function (error) {
        if (!!error.response.data.message)  toastr.error(error.response.data.message, 'Error!')
      })
      .then(function () {
        // always executed
      });
   }

  },
  mounted: function () {
    console.log('MOUNTED!')
    this.successModal = $(this.$refs.successModal);
    console.log(this.successModal);
  }
})
