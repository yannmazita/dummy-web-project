<template>
<div class="navbar bg-base-100">
  <div class="navbar-start">
    <div class="dropdown">
      <label tabindex="0" class="btn btn-ghost lg:hidden">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
      </label>
      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
        <li><a>Acceuil</a></li>
        <li><a>Agenda des matchs</a></li>
        <li><a>Comment s'inscire</a></li>
        <li><a>Nous contacter</a></li>
        <li><a>Boutique</a></li>
        <li>
          <a>Espace club</a>
          <ul class="p-2">
            <li><a>Gestion des salles</a></li>
            <li><a>Gestion des arbitres</a></li>
            <li><a>Gestion des adhérents</a></li>
            <li><a>Espace formation</a></li>
          </ul>
        </li>
      </ul>
    </div>
    <a class="btn btn-ghost text-xl">SCP Volley</a>
  </div>

  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1">
        <li tabindex="0"><a>Acceuil</a></li>
        <li><a>Agenda des matchs</a></li>
        <li><a>Comment s'inscire</a></li>
        <li><a>Nous contacter</a></li>
        <li><a>Boutique</a></li>
      <li>
        <details>
          <summary>Espace club</summary>
          <ul class="p-2">
            <li tabindex="0"><a>Gestion des salles</a></li>
            <li><a>Gestion des arbitres</a></li>
            <li><a>Gestion des adhérents</a></li>
            <li><a>Espace formation</a></li>
          </ul>
        </details>
      </li>
    </ul>
  </div>
  <div class="navbar-end">
  </div>
</div>
</template>

<script>
</script>    

<style>

</style>
