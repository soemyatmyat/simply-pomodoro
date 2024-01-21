const cacheName='PWA-Pomodoro'

// 1. install the service worker
self.addEventListener('install',(e)=> {
    console.log('[Service Worker] Installation Complete')
    e.waitUntil((async ()=>{
        const cache=await caches.open(cacheName)
        console.log('[Service Worker] Caching...')
        await cache.addAll(appShellFiles)
        console.log('[Service Worker] Cache Complete')
    })())
})

// 2. Activate the service worker 
self.addEventListener('activate',(e)=>{
    console.log('[Service Worker] Activated')
})

// 3. trigger based - fetch event fires every time any resources controlled by a sw is fetched
self.addEventListener('fetch',(e)=>{
    console.log('[Service Worker] Fetching Info...')
})
