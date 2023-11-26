<template>
    <div class="hero min-h-screen bg-base-200">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                <div class="card-body">
                <FormKit
                    type="form"
                    :config="{ validationVisibility: 'live'}"
                >
                    <FormKit
                        type="text"
                        name="login"
                        id="login"
                        label="Login"
                        help="Le nom d'utilisateur"
                        placeholder="richard.stallman"
                        validation="required"
                    />
                    <FormKit
                    type="password"
                    name="mdp"
                    label="Mot de passe"
                    help="Entrez votre mot de passe"
                    validation="required"
                    validation-visibility="live"
                    />
                </FormKit>
                </div>
            </div>
        </div>
    </div> 
</template>
