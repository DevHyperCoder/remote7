<script lang="ts">
	let msg: string;
	let err: string = '';
	let delay: string = '1000';

	const display = async (m: string) => {
		try {
			const { msg, status } = await (
				await fetch('/api/display', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ msg: m, delay })
				})
			).json();

			if (status === 'ERR') {
				err = msg;
			} else {
				err = '';
			}
		} catch (e: any) {
			err = e;
		}
	};
</script>

<div class="h-screen flex flex-col justify-between">
	<main class="w-1/2 mx-auto">
		<h1 class="text-5xl font-serif text-center py-10">Remote 7</h1>

		<div class="flex gap-4 my-4 justify-between">
			<div class="w-full">
				<input
					class="bg-gray-900 text-xl 
                    w-full
                    px-3 py-2
                    border border-1 border-gray-100
                  "
					type="text"
					bind:value={msg}
					placeholder="Enter character / message: "
				/>
				<p class="text-red-500 mt-1">{err}</p>
			</div>
			<button
				class="border border-1 border-green-500 px-3 py-2 rounded-md"
				on:click={() => display(msg)}>Display</button
			>
		</div>

		<div class="flex flex-col gap-2 my-10">
			<label class="text-slate-400 font-bold" for="delay-slider">Delay in ms: {delay}</label>
			<div class="flex gap-4">
				<input id="delay-slider" bind:value={delay} type="range" min="1" max="10000" />
				<input
					class="bg-gray-900 text-xl w-full px-3 py-2 border border-1 border-gray-100"
					id="delay-slider-numric"
					bind:value={delay}
					type="number"
				/>
			</div>
		</div>

		<p class="text-slate-400 font-bold mt-3 my-1">Commands:</p>
		<div class="flex gap-2">
			<button
				class="border border-1 border-green-500 px-3 py-2 rounded-md"
				on:click={() => display('BLINK ALL')}>BLINK ALL</button
			>
			<button
				class="border border-1 border-green-500 px-3 py-2 rounded-md"
				on:click={() => display('PATTERN')}>PATTERN</button
			>
			<button
				class="border border-1 border-green-500 px-3 py-2 rounded-md"
				on:click={() => display('OFF')}>TURN OFF</button
			>
		</div>
	</main>
	<footer class="mt-auto">
		<p class="font-bold text-center py-3">DevHyperCoder - 2022</p>
	</footer>
</div>
