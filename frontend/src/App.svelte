<script>
        import Router from 'svelte-spa-router'
        import Home from "./route/Home.svelte"
        import Detail from "./route/Detail.svelte"

        const routes = {
            '/': Home,
            '/detail/:question_id': Detail,
        }
</script>

<Router {routes}/>
