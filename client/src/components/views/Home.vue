<template>
  <div>
    <h1>Home</h1>
    <div class="cards">
      <router-link :to="{ name: 'sales' }">
        <div class="card">
          <md-card md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">Ventas generales</div>
              </md-card-header>

              <md-card-content>
                Detalles de todos los productos vendido incluyendo,
                identificador de venta, productos, fecha, monto y mesero
              </md-card-content>
            </md-ripple>
          </md-card>
        </div>
      </router-link>
      <router-link :to="{ name: 'categories' }">
        <div class="card">
          <md-card md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">Ventas agrupadas por categorias</div>
              </md-card-header>

              <md-card-content>
                Contiene cantidades vendidas e ingresos totales de cada
                categoria de productos vendidos
              </md-card-content>
            </md-ripple>
          </md-card>
        </div>
      </router-link>
      <router-link :to="{ name: 'products' }">
        <div class="card">
          <md-card md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">Ventas agrupadas por productos</div>
              </md-card-header>

              <md-card-content>
                Contiene cantidades vendidas e ingresos totales de cada producto
                vendido
              </md-card-content>
            </md-ripple>
          </md-card>
        </div>
      </router-link>
      <router-link :to="{ name: 'waiters' }">
        <div class="card">
          <md-card md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">Ventas agrupadas por meseros</div>
              </md-card-header>

              <md-card-content>
                Contiene cantidad de productos vendidos y recaudacion total de
                cada mesero
              </md-card-content>
            </md-ripple>
          </md-card>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "home-view",
};
</script>

<style scoped>
.cards {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin-inline: 10%;
}
.card {
    width: 35rem;
    padding: 10%;
}
</style>