import jspsych from "./jspsych";

export default function (payload, target = 'parallel') {
    console.log('Hell o people');
    // const payload = 125;
    const params = {
        setup: {
            detail: {
                target,
                action: 'setup',
                payload: payload.setup
            }
        },
        trigger: {
            detail: {
                target,
                action: 'trigger',
                payload: payload.trigger
            }
        }
    };
    return {
        setup: new CustomEvent('jspsych', params.setup),
        trigger: new CustomEvent('jspsych', params.trigger),
    };
}

function formatDate(date) {
    return `${date.getDay()}-${date.getMonth()}-${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}.${date.getMilliseconds()}`;
}
